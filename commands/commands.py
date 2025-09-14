import datetime
from utils import speak 


def handle_command(command):
    if "hello" in command:
        say_hello()

    elif "time" in command:
        tell_time()

    elif "exit" in command or "quit" in command:
        exit_program()
        return False
    else:
        speak('Okay')
    return True


def say_hello():
    speak("Hello! How are you today?")

def tell_time():
    now = datetime.datetime.now()
    speak(f"The time is {now.hour}:{now.minute}")

def exit_program():
    speak("Goodbye!")
