# Task 3 
# Basic Chatbot
# Create a text-based chatbot that can have
# conversations with users. You can use natural
# language processing libraries like NLTK or spaCy to
# make your chatbot more conversational

import random

def chatbot_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help?", "Nice to see you!"],
        "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thank you!", "I'm here to assist you!", "Feeling chatty today!"],
        "what is your name": ["I'm a chatbot! You can call me ChatBuddy.", "I am ChatBuddy, your virtual assistant.", "My name is ChatBuddy, nice to meet you!"],
        "what can you do": ["I can chat with you, answer basic questions, and keep you entertained!", 
                            "I can help with basic tasks, try asking me something!", 
                            "I can assist with your queries, try me!"],
        "tell me a joke": ["Why don’t scientists trust atoms? Because they make up everything!", 
                           "What do you call fake spaghetti? An impasta!", 
                           "Why did the math book look sad? Because it had too many problems!"],
        "where are you from": ["I'm from the digital world!", "I exist in the cloud, floating around in cyberspace!", "I live inside your computer!"],
        "what is your favorite color": ["I like all colors, but blue is quite nice!", "I don’t have eyes, but I hear red is cool!", "I like the color of the internet!"],
        "do you like music": ["I don’t have ears, but I hear music is amazing!", "I love anything that makes people happy!", "Music sounds great, what do you like?"],
        "who created you": ["I was created by a programmer like you!", "Someone smart wrote my code!", "I was built using Python!"],
        "what is your purpose": ["My purpose is to chat with you and make your day better!", "I’m here to assist and entertain you!", "I was made to have fun conversations!"],
        "bye": ["Goodbye! Have a great day!", "See you later!", "Take care!", "Bye! It was nice chatting with you!"]
    }

    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm not sure how to respond to that, but I'm learning!"

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
