from voice_recognition import listen
from Hackathon_22BTRCO006.src.intent_recognition import detect_intent
from task_executor import execute_command
from text_to_speech import speak

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    command = listen()
    if command:
        intent = detect_intent(command)
        execute_command(intent, command)
