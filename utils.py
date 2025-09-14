import pyttsx3 

engine = pyttsx3.init()

# Assistant speaks (pyttsx3)
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    
