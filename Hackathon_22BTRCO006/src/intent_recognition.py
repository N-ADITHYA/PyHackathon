import spacy

nlp = spacy.load("en_core_web_sm")

def detect_intent(command):
    doc = nlp(command)
    if "youtube" in command:
        return "open_youtube"
    elif "time" in command:
        return "tell_time"
    elif "joke" in command:
        return "tell_joke"
    elif "alarm" in command:
        return "set_alarm"
    elif "light" in command:
        return "control_lights"
    else:
        return "chatbot_response"
