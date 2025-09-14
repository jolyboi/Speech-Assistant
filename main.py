import speech_recognition as sr 
import pyttsx3 
from commands import commands
from utils import speak 

recognizer = sr.Recognizer() 

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
    running = True
    while running:
        command = listen()
        if command:
            running = commands.handle_command(command)
