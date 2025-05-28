# 🚀 AiTools Suite ✨

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/Flask-3.1.1-green.svg" alt="Flask 3.1.1">
  <img src="https://img.shields.io/badge/OpenAI-GPT--4o-orange.svg" alt="OpenAI GPT-4o">
  <img src="https://img.shields.io/badge/Google-Gemini-orange.svg" alt="Gemini-2.5-flash">
  <img src="https://img.shields.io/badge/AssemblyAI-AssemblyAI-orange.svg" alt="AssemblyAI">
  <br>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status: Active">
</div>

<p align="center">
  ✨ A powerful collection of AI-powered tools for content analysis, weather forecasting, task management, and more. ✨
</p>

<div align="center">
  <img src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake.svg" alt="GitHub Contribution Snake Animation" width="80%">
</div>

---

## 📋 Table of Contents 📚

- [🔍 Overview](#-overview)
- [📱 Applications](#-applications)
  - [🍎 FoodScanner](#-foodscanner)
  - [📄 WebSummary](#-websummary)
  - [🎬 VideoSum](#-videosum)
  - [☁️ AIWeather](#-aiweather)
  - [📝 TodoList/Journal](#-todolistjournal)
- [⚙️ Installation](#-installation)
- [🔐 Environment Setup](#-environment-setup)
- [📚 API Documentation](#-api-documentation)
- [🏗️ Architecture](#-architecture)
- [🔒 Security](#-security)


---

## 🔍 Overview 🌟

<div align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" alt="html5" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg" alt="css3" width="40" height="40"/>
  <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/>
</div>

🧠 **AiTools Suite** is a collection of AI-powered web applications designed to simplify various tasks through the power of artificial intelligence. Each tool in the suite leverages modern AI technologies like OpenAI's GPT models, Google's Gemini, AssemblyAI, and more to provide intelligent analysis and automation.

💡 The suite follows a consistent architecture with:
- 🧩 Modular design patterns
- 🌐 RESTful APIs with Swagger documentation
- 🔑 Secure environment variable management

---

## 📱 Applications 🛠️

### 🍎 FoodScanner 🥗

<div align="center">
  <img src="https://img.shields.io/badge/AI-Powered-brightgreen.svg" alt="AI-Powered">
  <img src="https://img.shields.io/badge/OpenAI-GPT--4o-orange.svg" alt="OpenAI GPT-4o">
</div>

**Description:** 📱 Scan food barcodes and get detailed nutritional analysis powered by OpenAI's GPT-4o.

**✨ Features:**
- 📷 Barcode scanning via web interface
- 🔄 Integration with OpenFoodFacts database
- 📊 Detailed nutritional analysis and health assessment
- ⚠️ Identification of potentially harmful ingredients
- 🌐 RESTful API with Swagger UI documentation
- 🤖 Uses OpenAI's GPT-4o for text generation

**🚀 Usage:**
```bash
cd foodscanner
python foodscan.py
# Access at http://localhost:5000
# API docs at http://localhost:5000/api/docs
```

### 📄 WebSummary 📝

<div align="center">
  <img src="https://img.shields.io/badge/AI-Powered-brightgreen.svg" alt="AI-Powered">
  <img src="https://img.shields.io/badge/OpenAI-GPT--4o-orange.svg" alt="OpenAI GPT-4o">
</div>

**Description:** 🔍 Summarize web page content with a single click using OpenAI's GPT-4o.

**✨ Features:**
- 🔗 URL-based content extraction
- 🧠 AI-powered summarization
- 📝 Clean, paragraph-format summaries
- 🌐 RESTful API with Swagger UI documentation
- 🤖 Uses OpenAI's GPT-4o for summarization

**🚀 Usage:**
```bash
cd WebSummary
python websummary.py
# Access at http://localhost:5001
# API docs at http://localhost:5001/api/docs
```

### 🎬 VideoSum 📹

<div align="center">
  <img src="https://img.shields.io/badge/AI-Powered-brightgreen.svg" alt="AI-Powered">
  <img src="https://img.shields.io/badge/OpenAI-GPT--4o-orange.svg" alt="OpenAI GPT-4o">
  <img src="https://img.shields.io/badge/AssemblyAI-Transcription-blue.svg" alt="AssemblyAI">
</div>

**Description:** 📽️ Download, transcribe, and summarize YouTube videos automatically.

**✨ Features:**
- 📥 YouTube video downloading
- 🔊 Audio extraction and transcription via AssemblyAI
- 🧠 AI-powered summarization with OpenAI's GPT-4o
- 💾 Output saving to text files
- 🌐 RESTful API with Swagger UI documentation
- 🤖 Uses OpenAI's GPT-4o for summarization

**🚀 Usage:**
```bash
cd videosum
python vdsum.py
# Access at http://localhost:5100
# API docs at http://localhost:5100/api/docs
```

### ☁️ AIWeather 🌦️

<div align="center">
  <img src="https://img.shields.io/badge/AI-Powered-brightgreen.svg" alt="AI-Powered">
  <img src="https://img.shields.io/badge/Google-Gemini-orange.svg" alt="Google Gemini">
</div>

**Description:** 🌤️ Get detailed weather forecasts and air quality information with AI-powered insights.

**✨ Features:**
- 📍 Current location detection
- 🌡️ Weather and air quality data retrieval
- 💬 Natural language queries about weather conditions
- 📱 Modern, responsive UI
- 🤖 Uses Google Gemini for text generation

**🚀 Usage:**
```bash
cd AIWeather
# Open AIWeather.html in a web browser
```

### 📝 TodoList/Journal 📓

<div align="center">
  <img src="https://img.shields.io/badge/AI-Powered-brightgreen.svg" alt="AI-Powered">
  <img src="https://img.shields.io/badge/Google-Gemini-orange.svg" alt="Google Gemini">
</div>

**Description:** ✅ AI-enhanced task management and journaling application.

**✨ Features:**
- ✏️ Task creation and management
- 📔 Journal entry capabilities
- 🧠 AI-powered insights and suggestions
- 🎨 Clean, intuitive interface
- 🤖 Uses Google Gemini for text generation

**🚀 Usage:**
```bash
cd todolist
# Open index.html in a web browser
```

---

## ⚙️ Installation 🔧

<div align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="git" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
</div>

1. 📥 **Clone the repository:**
```bash
git clone https://github.com/yourusername/AiTools.git
cd AiTools
```

2. 📦 **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. 🔐 **Set up environment variables** (see [Environment Setup](#-environment-setup))

4. 🚀 **Run the desired application** (see individual application instructions above)

---

## 🔐 Environment Setup 🛠️

<div align="center">
  <img src="https://img.shields.io/badge/Security-First-red.svg" alt="Security First">
</div>

🔑 Create a `.env` file in the root directory with the following variables:

```
# 🤖 OpenAI API
OPENAI_API_KEY=your_openai_api_key

# 🎙️ AssemblyAI API
ASSEMBLYAI_API_KEY=your_assemblyai_api_key

# 🧠 Google Gemini API
GEMINI_API_KEY=your_gemini_api_key

# ☁️ Weather APIs
OPENWEATHER_API_KEY=your_openweather_api_key
AQICN_API_KEY=your_aqicn_api_key
```

💻 For JavaScript applications, the environment variables are loaded from `env-config.js`.

---

## 📚 API Documentation 📋

<div align="center">
  <img src="https://img.shields.io/badge/Swagger-UI-green.svg" alt="Swagger UI">
  <img src="https://img.shields.io/badge/REST-API-blue.svg" alt="REST API">
</div>

🌐 Each application with an API (FoodScanner, WebSummary, VideoSum) includes Swagger UI documentation accessible at:

- 🍎 FoodScanner: `http://localhost:5000/api/docs`
- 📄 WebSummary: `http://localhost:5001/api/docs`
- 🎬 VideoSum: `http://localhost:5100/api/docs`

✨ These interactive documentation pages allow you to:
- 🔍 View available endpoints
- 🧪 Test API calls directly from the browser
- 📊 See request/response models
- 📝 Understand API parameters

---

## 🏗️ Architecture 🔨

<div align="center">
  <img src="https://img.shields.io/badge/Design-Modular-blue.svg" alt="Modular Design">
  <img src="https://img.shields.io/badge/Pattern-MVC-green.svg" alt="MVC Pattern">
</div>

🧩 The AiTools Suite follows a consistent architecture across applications:

```
application/
├── 📄 app.py (or similar main file)
├── 🧠 services.py (business logic)
├── 🔧 utils.py (utilities and helpers)
├── 🎨 templates/ (HTML templates)
└── 🖼️ static/ (CSS, JS, images)
```

🌟 **Key architectural principles:**
- 🧩 **Modular Design**: Separation of concerns between UI, business logic, and utilities
- 🌐 **RESTful APIs**: Consistent API design with proper status codes and error handling
- 🔐 **Environment Management**: Centralized environment variable handling
- 📚 **Documentation**: Swagger UI for API documentation

---

## 🔒 Security 🛡️

<div align="center">
  <img src="https://img.shields.io/badge/Security-Best_Practices-red.svg" alt="Security Best Practices">
  <img src="https://img.shields.io/badge/Data-Protected-blue.svg" alt="Data Protected">
</div>

🔐 The AiTools Suite implements several security best practices:

- 🔑 **API Key Management**: All API keys are stored in environment variables
- ✅ **Input Validation**: Proper validation of user inputs
- 🚫 **Error Handling**: Secure error handling that doesn't expose sensitive information
- 🙈 **.gitignore**: Configuration to prevent sensitive files from being committed

---

<div align="center">
  <img src="https://img.shields.io/badge/Made_with-❤️-red.svg" alt="Made with Love">
  <img src="https://img.shields.io/badge/Powered_by-AI-blue.svg" alt="Powered by AI">
  <br>
  <p>Created with ❤️ by SoraKun</p>
</div>

<div align="center">
  <a href="https://github.com/yourusername/AiTools/stargazers"><img src="https://img.shields.io/github/stars/yourusername/AiTools?style=social" alt="Stars"></a>
  <a href="https://github.com/yourusername/AiTools/network/members"><img src="https://img.shields.io/github/forks/yourusername/AiTools?style=social" alt="Forks"></a>
  <a href="https://github.com/yourusername/AiTools/issues"><img src="https://img.shields.io/github/issues/yourusername/AiTools?style=social" alt="Issues"></a>
</div>
