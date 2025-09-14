import pyttsx3

engine = pyttsx3.init('nsss')
print('hi')
engine.say("Hello, testing my voice")
engine.runAndWait()