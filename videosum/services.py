import moviepy.editor as mp
import assemblyai as aai
import yt_dlp
import os
import subprocess
from typing import Dict, Any, Optional, List
from utils import generate_text_with_openai, get_assemblyai_key

def download_youtube_video(video_url: str, folder_path: str) -> List[str]:
    """
    Download a YouTube video using yt-dlp.
    
    Args:
        video_url: URL of the YouTube video
        folder_path: Path to save the downloaded video
        
    Returns:
        List of downloaded file paths
    """
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': f'{folder_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            # Get the filename from the info dict
            if 'entries' in info:  # It's a playlist
                filenames = [entry.get('requested_downloads', [{}])[0].get('filepath', '') 
                            for entry in info['entries']]
                return filenames
            else:  # It's a single video
                filename = info.get('requested_downloads', [{}])[0].get('filepath', '')
                return [filename] if filename else []
    except Exception as e:
        print(f"Error downloading video: {e}")
        return []

def convert_video_to_audio(video_path: str) -> str:
    """
    Convert video file to audio (WAV) format.
    
    Args:
        video_path: Path to the video file
        
    Returns:
        Path to the generated audio file
    """
    try:
        # Get the base path without extension
        base_path = os.path.splitext(video_path)[0]
        audio_path = f"{base_path}.wav"
        
        # Extract audio using moviepy
        video = mp.VideoFileClip(video_path)
        audio_file = video.audio
        audio_file.write_audiofile(audio_path)
        
        print(f"Converted {video_path} to audio: {audio_path}")
        return audio_path
    except Exception as e:
        print(f"Error converting video to audio: {e}")
        return ""

def transcribe_audio(audio_path: str) -> str:
    try:
        # Configure AssemblyAI
        aai.settings.api_key = get_assemblyai_key()
        transcriber = aai.Transcriber()
        
        # Transcribe the audio file
        print(f"Transcribing audio: {audio_path}")
        transcript = transcriber.transcribe(audio_path)
        
        if transcript.text:
            return transcript.text
        else:
            return "No transcription available."
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return f"Error transcribing audio: {str(e)}"

def summarize_transcript(transcript: str) -> str:
    if not transcript or transcript.startswith("Error"):
        return "Could not generate summary due to transcription error."
    
    prompt = f"""
    Given the following transcript extracted from a video, provide a concise summary in less than 450 words.
    Keep your output in paragraph format (not bullet points).
    Focus on the main points, key information, and overall message of the content.
    
    Transcript: {transcript}
    """
    
    print("Summarizing transcript...")
    return generate_text_with_openai(prompt)

def append_to_file(summary: str, video_name: str, output_file: str = r"D:\AiTools\videosum\output.txt") -> None:
    try:
        with open(output_file, 'a', encoding="utf-8") as f:
            f.write(f"Video: {video_name}\n")
            f.write(summary)
            f.write("\n\n")
        print(f"Summary appended to {output_file}")
    except Exception as e:
        print(f"Error appending to file: {e}")

def process_video(video_url: str, folder_path: str = r"D:\AiTools\videosum\videos") -> Dict[str, Any]:
    try:
        # Download the video
        downloaded_files = download_youtube_video(video_url, folder_path)
        
        if not downloaded_files:
            return {"result": "Error: Could not download the video."}
        
        video_path = downloaded_files[0]
        video_name = os.path.basename(video_path)
        
        # Convert to audio
        audio_path = convert_video_to_audio(video_path)
        if not audio_path:
            return {"result": "Error: Could not convert video to audio."}
        
        # Transcribe the audio
        transcript = transcribe_audio(audio_path)
        if transcript.startswith("Error"):
            return {"result": transcript}
        
        # Summarize the transcript
        summary = summarize_transcript(transcript)
        
        # Append to output file
        append_to_file(summary, video_name)
        
        # Clean up files if needed
        # (Uncomment if you want to delete the files after processing)
        # cleanup_files(video_path, audio_path)
        
        return {"result": summary}
    except Exception as e:
        print(f"Error processing video: {e}")
        return {"result": f"Error processing video: {str(e)}"}

def cleanup_files(video_path: str, audio_path: str) -> None:
    try:
        if os.path.exists(video_path):
            os.remove(video_path)
        if os.path.exists(audio_path):
            os.remove(audio_path)
        print("Temporary files cleaned up.")
    except Exception as e:
        print(f"Error cleaning up files: {e}")
