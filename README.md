# 🎙️ Assistant-Python

**Assistant-Python** is a smart virtual assistant developed in Python. It leverages Google's **Gemini 1.5 Flash** model to process natural language and perform automated tasks via voice commands.

---

## ✨ Features

- **🧠 AI Powered:** Advanced queries using the Google Generative AI (Gemini) API.
- **🎤 Voice Control:** Precise speech recognition using the `SpeechRecognition` library.
- **🗣️ Voice Feedback:** The assistant talks back to you using Text-to-Speech (TTS) via `pyttsx3`.
- **📖 Dynamic Learning:** If the assistant doesn't know an answer, you can teach it! It saves new responses to a local file (`responses.txt`).
- **🎵 Multimedia:** Play music on YouTube and open websites automatically.
- **📅 Utilities:** Get the current time, date, and daily motivational quotes.

---

## 🚀 Installation & Setup

Follow these steps to get KeepEar up and running on your local machine.

### 1. Clone the Repository
Open your terminal and run:
```bash
git clone [https://github.com/Carlos743251/Assistant-Python.git](https://github.com/Carlos743251/Assistant-Python.git)
```
### 2. Install System Dependencies
To ensure the microphone works correctly, you need specific audio tools depending on your OS:

* On Linux (Ubuntu/Debian):
```Bash
sudo apt-get install python3-pyaudio portaudio19-dev libasound2-dev
```
* On Windows: If you encounter errors installing PyAudio, download the .whl file matching your Python version from here and install it manually.

### 3. Install Python Libraries
Install all required libraries with a single command:

```Bash
pip install speechrecognition google-generativeai pyttsx3 requests
```
