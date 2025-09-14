import datetime
from utils import speak 


def handle_command(command):
    print('command handled')
    if "hello" in command:
        say_hello()

    elif "time" in command:
        tell_time()

    elif "exit" in command or "quit" in command:
        return exit_program()
    else:
        print("Command not recognized.")
    return True


def say_hello():
    speak("Hello! How are you today?")

def tell_time():
    now = datetime.datetime.now()
    speak(f"The time is {now.hour}:{now.minute}")

def exit_program():
    speak("Goodbye!")
    return False 
