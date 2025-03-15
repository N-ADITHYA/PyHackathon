import webbrowser
import datetime
import random
import time
from text_to_speech import speak
from Hackathon_22BTRCO006.src.chatbot import chatbot_response

def execute_command(intent, command):
    if intent == "open_youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif intent == "tell_time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif intent == "tell_joke":
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you get when you cross a snowman and a vampire? Frostbite!",
            "Why was the math book sad? It had too many problems."
        ]
        joke = random.choice(jokes)
        speak(joke)
    elif intent == "set_alarm":
        words = command.split()
        for word in words:
            if word.isdigit():
                alarm_time = int(word)
                speak(f"Setting an alarm for {alarm_time} seconds from now.")
                time.sleep(alarm_time)
                speak("Time's up!")
                break
    elif intent == "control_lights":
        if "on" in command:
            speak("Turning on the lights. Oh wait, I don't actually have smart lights!")
        elif "off" in command:
            speak("Turning off the lights. Just pretend it's dark now!")
    else:
        response = chatbot_response(command)
        speak(response)
