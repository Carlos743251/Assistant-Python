import speech_recognition as sr
import google.generativeai as genai
import pyttsx3
import datetime
import webbrowser
import requests
from os import system
# Initialization
recognizer = sr.Recognizer()
process = None
engine = pyttsx3.init()
engine.setProperty('rate', 150)

genai.configure(api_key="your_gemini_api_key")  # Replace with your actual key

accent_map = str.maketrans("áéíóúü", "aeiouu")

def load_dictionary():
    responses = {}
    try:
        with open(response_file, 'r') as file:
            for line in file:
                if line.strip():
                    key, value = line.strip().split(':')
                    responses[key.strip()] = value.strip()
    except FileNotFoundError:
        pass
    return responses

def add_response(responses, key, value):
    responses[key] = value

def save_responses(responses, response_file):
    with open(response_file, 'w') as file:
        for key, value in responses.items():
            file.write(f"{key}: {value}\n")

def query_gemini(command):
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
        response = model.generate_content(command)
        return response.text.strip()
    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry, an error occurred while querying Gemini."

def speak(text):
    engine.say(text)
    engine.runAndWait()

def play_on_youtube(song):
    query = song.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    print("AI: Opening YouTube")
    speak("Opening YouTube")

def execute_command(command):
    global process
    if command in ("exit", "cancel"):
        print("AI: Goodbye. See you later.")
        speak("Goodbye. See you later.")
        exit()
    elif "time" in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(f"AI: The time is {time}")
        speak(f"The time is {time}")
    elif "search" in command:
        ai_response = query_gemini(command)
        print("AI:", ai_response)
        speak(ai_response)
    elif command in ("date", "what day is it"):
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        print(f"AI: The date is {date}")
        speak(f"The date is {date}")
    elif "open" in command:
        site = command.replace("open", "").strip()
        if "youtube" in site:
            webbrowser.open("https://youtube.com")
            print("Opening YouTube")
            speak("Opening YouTube")
        elif "google" in site:
            webbrowser.open("https://google.com")
            print("Opening Google")
            speak("Opening Google")
    elif "quote" in command:
        response = requests.get("https://frasedeldia.azurewebsites.net/api/phrase")
        data = response.json()
        print(data["phrase"])
        speak(data["phrase"])
    elif "play" in command:
        song = command.replace("play", "").strip()
        play_on_youtube(song)
    else:
        responses = load_dictionary()
        if command in responses:
            reply = responses.get(command)
            print(f"AI: {reply}")
            speak(reply)
        else:
            print("AI: I don't recognize that command. I'm still learning...")
            speak("I don't recognize that command. I'm still learning...")
            print("AI: Can you please repeat what you said so I can add it to my responses?")
            speak("Can you please repeat what you said so I can add it to my responses?")
            key = listen()
            while key == "":
                key = listen()
            print("AI: Great. Now, what should I reply?")
            speak("Great. Now, what should I reply?")
            value = listen()
            while value == "":
                value = listen()
            add_response(responses, key, value)
            save_responses(responses, response_file)
            print("AI: Got it! I’ve saved it.")
            speak("Got it! I’ve saved it.")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        x = recognizer.recognize_google(audio, language="en-US").lower()
        command = x.translate(accent_map)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Didn't catch that.")
        return ""
    except sr.RequestError as e:
        print(f"Request error: {e}")
        return ""

try:
    # Main program
    response_file = 'responses.txt'
    system('cls') #clear console in windows
    print("Hi, how can I help you?")
    speak("Hi, how can I help you?")
    while True:
        command = listen()
        while command == "":
            command = listen()
        execute_command(command)
except:
    print("\n\nProgram terminated\n\n")
