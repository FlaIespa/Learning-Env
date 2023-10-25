import nltk
import random
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you.', 'I am just a computer program, but I am functioning properly.']),
    (r'what is your name', ['I am a chatbot.', 'My name is Chatbot.']),
    (r'who are you', ['I am a chatbot.', 'I am an AI chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
    (r'can you help me?', ['Of course! What do you need?', ' Of course! How can I help you?']),
    (r'I am not feeling good', ['I am sorry to hear that can you tell me more about what you are feeling?', 'I understand. Do you want to tell me more about how you are feeling?']),
    (r'(.*)', ['I am sorry, I do not understand.', 'Please try again.']),
]

# Create a Chat instance
chatbot = Chat(patterns, reflections)

# Main loop for interacting with the chatbot
print("Hello! I'm your chatbot. You can type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
