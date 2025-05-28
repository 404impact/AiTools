from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from services import process_video
from utils import load_env
from typing import Dict, Any
import os

# Load environment variables
load_env()

# Ensure videos directory exists
os.makedirs(r"D:\AiTools\videosum\videos", exist_ok=True)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Flask-RestX API with Swagger UI
api = Api(
    app,
    version='1.0',
    title='VideoSum API',
    description='API for downloading, transcribing, and summarizing YouTube videos',
    doc='/api/docs',  # Swagger UI will be available at this endpoint
    prefix='/api'
)

# Create namespaces for organizing endpoints
main_ns = api.namespace('', description='Main operations')
video_ns = api.namespace('video', description='Video summarization operations')

# Define models for request/response documentation
url_model = video_ns.model('UrlInput', {
    'url': fields.String(required=True, description='The YouTube video URL to summarize', 
                         example='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
})

summary_model = video_ns.model('SummaryOutput', {
    'result': fields.String(description='Summarized content from the video')
})

error_model = video_ns.model('ErrorResponse', {
    'error': fields.String(description='Error message')
})

# API endpoints with Swagger documentation
@video_ns.route('')
class VideoSummary(Resource):
    @video_ns.doc('get_summary_with_query_param')
    @video_ns.param('url', 'The YouTube video URL to summarize', _in='query')
    @video_ns.response(200, 'Success', summary_model)
    @video_ns.response(400, 'Invalid Input', error_model)
    def get(self) -> Dict[str, Any]:
        """Get a summary of a YouTube video using query parameter."""
        url = request.args.get('url')
        
        if not url:
            return {"error": "No URL provided"}, 400
            
        print(f"Processing video URL (GET): {url}")
        return process_video(url)
    
    @video_ns.expect(url_model)
    @video_ns.response(200, 'Success', summary_model)
    @video_ns.response(400, 'Invalid Input', error_model)
    def post(self) -> Dict[str, Any]:
        """Get a summary of a YouTube video using JSON body."""
        data = request.json
        url = data.get('url')
        
        if not url:
            return {"error": "No URL provided"}, 400
            
        print(f"Processing video URL (POST): {url}")
        return process_video(url)

# Legacy route for backward compatibility
@app.route('/submit/', methods=['GET'])
def submit():
    """Legacy endpoint for backward compatibility."""
    video_url = request.args.get('query')
    print(f"Legacy endpoint called with URL: {video_url}")
    
    if not video_url:
        return {"result": "No URL provided"}
        
    result = process_video(video_url)
    return result

if __name__ == '__main__':
    # Enable debug mode to see detailed error messages
    app.run(debug=True, port=5100)

# ask_from = ask_from + 1
