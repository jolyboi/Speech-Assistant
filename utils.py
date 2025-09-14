import pyttsx3 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[9].id)

# Assistant speaks (pyttsx3)
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    
