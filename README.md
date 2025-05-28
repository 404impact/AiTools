# 🚀 AiTools Suite

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/Flask-3.1.1-green.svg" alt="Flask 3.1.1">
  <img src="https://img.shields.io/badge/OpenAI-GPT--4o-orange.svg" alt="OpenAI GPT-4o">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</div>

<p align="center">
  A powerful collection of AI-powered tools for content analysis, weather forecasting, task management, and more.
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Applications](#-applications)
  - [FoodScanner](#-foodscanner)
  - [WebSummary](#-websummary)
  - [VideoSum](#-videosum)
  - [AIWeather](#-aiweather)
  - [TodoList/Journal](#-todolistjournal)
- [Installation](#-installation)
- [Environment Setup](#-environment-setup)
- [API Documentation](#-api-documentation)
- [Architecture](#-architecture)
- [Security](#-security)
- [License](#-license)

---

## 🔍 Overview

AiTools Suite is a collection of AI-powered web applications designed to simplify various tasks through the power of artificial intelligence. Each tool in the suite leverages modern AI technologies like OpenAI's GPT models, Google's Gemini, AssemblyAI, and more to provide intelligent analysis and automation.

The suite follows a consistent architecture with modular design patterns, RESTful APIs with Swagger documentation, and secure environment variable management.

---

## 📱 Applications

### 🍎 FoodScanner

**Description:** Scan food barcodes and get detailed nutritional analysis powered by OpenAI's GPT-4o.

**Features:**
- Barcode scanning via web interface
- Integration with OpenFoodFacts database
- Detailed nutritional analysis and health assessment
- Identification of potentially harmful ingredients
- RESTful API with Swagger UI documentation

**Usage:**
```bash
cd foodscanner
python foodscan.py
# Access at http://localhost:5000
# API docs at http://localhost:5000/api/docs
```

### 📄 WebSummary

**Description:** Summarize web page content with a single click using OpenAI's GPT-4o.

**Features:**
- URL-based content extraction
- AI-powered summarization
- Clean, paragraph-format summaries
- RESTful API with Swagger UI documentation

**Usage:**
```bash
cd WebSummary
python websummary.py
# Access at http://localhost:5001
# API docs at http://localhost:5001/api/docs
```

### 🎬 VideoSum

**Description:** Download, transcribe, and summarize YouTube videos automatically.

**Features:**
- YouTube video downloading
- Audio extraction and transcription via AssemblyAI
- AI-powered summarization with OpenAI's GPT-4o
- Output saving to text files
- RESTful API with Swagger UI documentation

**Usage:**
```bash
cd videosum
python vdsum.py
# Access at http://localhost:5100
# API docs at http://localhost:5100/api/docs
```

### ☁️ AIWeather

**Description:** Get detailed weather forecasts and air quality information with AI-powered insights.

**Features:**
- Current location detection
- Weather and air quality data retrieval
- Natural language queries about weather conditions
- Modern, responsive UI

**Usage:**
```bash
cd AIWeather
# Open AIWeather.html in a web browser
```

### 📝 TodoList/Journal

**Description:** AI-enhanced task management and journaling application.

**Features:**
- Task creation and management
- Journal entry capabilities
- AI-powered insights and suggestions
- Clean, intuitive interface

**Usage:**
```bash
cd todolist
# Open index.html in a web browser
```

---

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AiTools.git
cd AiTools
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (see [Environment Setup](#-environment-setup))

4. Run the desired application (see individual application instructions above)

---

## 🔐 Environment Setup

Create a `.env` file in the root directory with the following variables:

```
# OpenAI API
OPENAI_API_KEY=your_openai_api_key

# AssemblyAI API
ASSEMBLYAI_API_KEY=your_assemblyai_api_key

# Google Gemini API (optional, for legacy support)
GEMINI_API_KEY=your_gemini_api_key

# Weather APIs
OPENWEATHER_API_KEY=your_openweather_api_key
AQICN_API_KEY=your_aqicn_api_key
```

For JavaScript applications, the environment variables are loaded from `env-config.js`.

---

## 📚 API Documentation

Each application with an API (FoodScanner, WebSummary, VideoSum) includes Swagger UI documentation accessible at:

- FoodScanner: `http://localhost:5000/api/docs`
- WebSummary: `http://localhost:5001/api/docs`
- VideoSum: `http://localhost:5100/api/docs`

These interactive documentation pages allow you to:
- View available endpoints
- Test API calls directly from the browser
- See request/response models
- Understand API parameters

---

## 🏗️ Architecture

The AiTools Suite follows a consistent architecture across applications:

```
application/
├── app.py (or similar main file)
├── services.py (business logic)
├── utils.py (utilities and helpers)
├── templates/ (HTML templates)
└── static/ (CSS, JS, images)
```

Key architectural principles:
- **Modular Design**: Separation of concerns between UI, business logic, and utilities
- **RESTful APIs**: Consistent API design with proper status codes and error handling
- **Environment Management**: Centralized environment variable handling
- **Documentation**: Swagger UI for API documentation

---

## 🔒 Security

The AiTools Suite implements several security best practices:

- **API Key Management**: All API keys are stored in environment variables
- **Input Validation**: Proper validation of user inputs
- **Error Handling**: Secure error handling that doesn't expose sensitive information
- **.gitignore**: Configuration to prevent sensitive files from being committed

---

<div align="center">
  <p>Created with ❤️ by SoraKun</p>
</div>
