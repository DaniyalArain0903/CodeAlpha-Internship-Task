# Task 3 
# Basic Chatbot
# Create a text-based chatbot that can have
# conversations with users. You can use natural
# language processing libraries like NLTK or spaCy to
# make your chatbot more conversational


import random

def chatbot_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
        "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thank you!"],
        "what is your name": ["I'm a chatbot! You can call me ChatBuddy.", "I am ChatBuddy, your virtual assistant."],
        "bye": ["Goodbye! Have a great day!", "See you later!"]
    }
    
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm not sure how to respond to that."

def chat():
    print("ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye!")
            break
        print("ChatBot:", chatbot_response(user_input))

if __name__ == "__main__":
    chat()
