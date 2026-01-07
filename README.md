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

### 3. Install Python Libraries
Install all required libraries with a single command:

```Bash
pip install speechrecognition google-generativeai pyttsx3 requests
```
## 🗝️ API Key Configuration

To enable the AI features, you need a Google Gemini API Key:

### 1. Go to [Google AI Studio.](https://aistudio.google.com/)

### 2. Generate your API Key.

### 3. In the `Assistant.py` file, find the following line and replace the placeholder:
```Python
genai.configure(api_key="YOUR_API_KEY_HERE")
```
###  ⚠️ SECURITY NOTE: Never share your API Key publicly. It is recommended to use environment variables for better security.

## 🛠️ Usage & Commands 
###To start the assistant, run:
```bash
python main.py
```
###When the program displays "Listening...", you can use the following voice commands:

| Command | Action |
| :--- | :--- |
| `time` | The assistant tells you the current time. |
| `date` / `what day is it` | The assistant tells you today's date (DD/MM/YYYY). |
| `search [your query]` | Sends your question to Gemini AI for an intelligent answer. |
| `open youtube` | Opens the YouTube homepage in your default browser. |
| `open google` | Opens the Google search engine in your default browser. |
| `play [song/artist]` | Searches and plays the specific video on YouTube. |
| `quote` | Fetches and recites a random motivational quote. |
| `exit` / `cancel` | Stops the program and says goodbye. |

## 🧠 Learning Mode
If you say something KeepEar doesn't recognize, it will enter Learning Mode:

### 1. The assistant will say: "I don't recognize that command..."

### 2. It will ask you to repeat what you said to confirm the trigger.

### 3. It will then ask what the reply should be.

### 4. Done! The data is saved to responses.txt and the assistant will remember it next time.
