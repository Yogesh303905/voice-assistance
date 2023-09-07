import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
recognizer = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            return ""

# Main loop
while True:
    user_input = listen().lower()
    
    if "hello"  in user_input:
        speak("Hello! How can I assist you?")
    elif "hii" in user_input:
        speak("Hello! How can I assist you?")
    elif "what is your name" in user_input:
        speak("I'm your Python voice assistant.")
    elif "how are you" in user_input:
        speak("I'm just a computer program, but I'm here to help you.")
    elif "tell me a joke" in user_input:
        speak("Why don't scientists trust atoms? Because they make up everything!")
    elif "search Google for" in user_input:
        query = user_input.replace("search Google for", "")
        speak(f"Searching Google for {query}...")
    elif "exit" in user_input or "goodbye" in user_input:
        speak("Goodbye!")
        break
    else:
        speak("I'm not sure how to help with that.")
