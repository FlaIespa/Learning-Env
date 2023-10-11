import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
psychologist = Chat([
    [
        r'I feel (.*)',
        ['I'm here to listen. Can you tell me more about how you feel?', 'I see. What's been bothering you?']
    ],
    [
        r'(.*)(help|advice|tips)(.*)',
        ['I can offer some general mental health tips. Would you like to hear them?']
    ],
    [
        r'yes',
        ['Sure! Here are some tips:\n1. Practice deep breathing exercises.\n2. Reach out to friends and family for support.\n3. Consider talking to a professional therapist.\n4. Engage in regular physical activity.\n5. Maintain a healthy diet and get enough sleep.']
    ],
    [
        r'no',
        ['Alright, if you change your mind, feel free to ask for tips anytime.']
    ],
    [
        r'bye',
        ['Take care. If you need anything else, don\'t hesitate to return.']
    ],
], reflections)

# Main chat loop
print("Hello, I'm here to provide mental health tips. You can tell me how you feel, and I'll do my best to assist you. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = psychologist.respond(user_input)
    print("Bot: " + response)
