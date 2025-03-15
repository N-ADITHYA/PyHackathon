from transformers import pipeline

chatbot = pipeline("text-generation", model="distilgpt2")

def chatbot_response(command):
    response = chatbot(command, max_length=50, num_return_sequences=1)[0]['generated_text']
    return response
