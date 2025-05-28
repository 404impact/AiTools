import { GoogleGenerativeAI } from "@google/generative-ai";

// Access environment variables from window.ENV
const gemini_key = window.ENV?.GEMINI_API_KEY || "AIzaSyDgRI4UVzfXMNAksUNgXS3K5ITkAoPqP74";

document.addEventListener("DOMContentLoaded", () => {
    loadEntries();
});

function addEntry() {
    const titleInput = document.getElementById("entryTitle");
    const entryInput = document.getElementById("entryInput");

    const titleText = titleInput.value.trim();
    const entryText = entryInput.value.trim();

    if (titleText === "" || entryText === "") {
        alert("Please enter both title and journal entry!");
        return;
    }

    const now = new Date();
    const timestamp = now.toLocaleString(); // Format: MM/DD/YYYY, HH:MM:SS AM/PM

    // Convert bullet points into an array of lines (if it has new lines)
    let entryLines = entryText.includes("\n") ? entryText.split("\n").map(line => line.trim()) : [entryText];

    let entries = JSON.parse(localStorage.getItem("journalEntries")) || [];
    entries.unshift({ title: titleText, entry: entryLines, time: timestamp }); // Add to the beginning
    localStorage.setItem("journalEntries", JSON.stringify(entries));
    
    titleInput.value = "";
    entryInput.value = "";
    loadEntries();
    
}

function loadEntries() {
    const list = document.getElementById("journalList");
    list.innerHTML = "";

    let entries = JSON.parse(localStorage.getItem("journalEntries")) || [];

    entries.forEach((entry, index) => {
        const li = document.createElement("li");

        const title = document.createElement("h3");
        title.textContent = entry.title;

        const contentList = document.createElement("ul");

        // 🔥 FIX: Ensure entry.entry is an array before looping 🔥
        const entryArray = Array.isArray(entry.entry) ? entry.entry : [entry.entry];

        entryArray.forEach(line => {
            const item = document.createElement("li");
            item.textContent = line;
            contentList.appendChild(item);
        });

        const time = document.createElement("small");
        time.textContent = `${entry.time}`;

        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Delete";
        deleteBtn.onclick = () => deleteEntry(index);

        li.appendChild(title);
        li.appendChild(contentList);
        li.appendChild(time);
        li.appendChild(deleteBtn);
        list.appendChild(li);
    });
}

function deleteEntry(index) {
    let entries = JSON.parse(localStorage.getItem("journalEntries")) || [];
    entries.splice(index, 1);
    localStorage.setItem("journalEntries", JSON.stringify(entries));
    loadEntries();
}


let summarizeEntry = () =>{
    let data = document.getElementById("entryInput");
    let datatext = data.value.trim();
    console.log(datatext)
    if(datatext === ""){
        alert("hey I cannot summarize something empty :)");
        return;
    }
    // gemini code from here:
    const genAI = new GoogleGenerativeAI(gemini_key);

    const gemini_run = async (datatext) => {

        // console.log(datatext)
        // For text-only input, use the gemini-pro model
        const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash"});
        const prompt = ` You are a note making student who reads contents of a book from the following data:${datatext} and writes a note based on the data in bullet points. Strictly do not leave any space between the lines and do not use asterisk anywhere and do not use any bullet icons not even hyphen.`
        const result = await model.generateContent(prompt);
        const response = await result.response;
        const text = response.text();
        // console.log(text);
        document.getElementById("entryInput").value = text;
        // console.log(debug)
    }

    gemini_run(datatext)
}

document.getElementById("summarize").addEventListener("click", () =>{summarizeEntry()})
document.getElementById("addentry").addEventListener("click", () =>{addEntry()})