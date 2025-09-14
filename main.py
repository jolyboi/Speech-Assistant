import speech_recognition as sr 
import pyttsx3 

recognizer = sr.Recognizer() 
engine = pyttsx3.init()

# Assistant speaks (pyttsx3)
def speak(text):
    engine.say(text)
    engine.runAndWait()
    

# Assistant listens
def listen():
    with sr.Microphone() as source: 
        print('Listening...')
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)  
            print(f'You: {command}')
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            return ""





# Run the file 
if __name__ == "__main__":
    speak("Hello! I am your assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            else:
                speak(f"You said: {command}")

