import random
from nltk.chat.util import Chat, reflections
from flask import Flask, request, jsonify

motivational_quotes = [ "Whatever you do, always give 100%. Unless you're are donating blood", 
                       "People often say that motivation doesn’t last. Well, neither does bathing — that’s why we recommedn it daily.",
                       "If you are going through hell, keep going.",
                       "My advice is not to wait to be struck by an idea. If you're a writer, you sit down and damn well decide to have an idea. That's the way to get an idea.",
                       "Do or do not. There is not try.",
                       "Creativity is a wild mind and a displicined eye.",
                       "You can't wait for inspiration. You have to go after it with a club.",
                       "A peacock that rest o his tail feathers is just another turkey.",
                       "So long as your desire to explore is greater than your desire to not screw up, you're on the right track.",
                       "It’s not whether you get knocked down; it's whether you get up.",
                       "Even if you're on the right track, you will get run over if you just sit there.",
                       "Don't do what you want. Do what you don't want. Do what you're trained not to want. Do the things that scare you the most.",
                       "Procrastination is the thief of time, collar him.",
                       "It ain't over til it's over."
]
# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello! How can I support you today?', 'Hi there! How can I assist you?', 'Hey! How are you feeling today?']),
    (r'how are you', ["I'm here to help you. How are you feeling?", "I'm a chatbot, but I'm here to listen. How can I support you?"]),
    (r'what is your name', ["I'm your supportive chatbot. What's on your mind?", "I'm here to talk to you. What's your name?"]),
    (r'who are you', ["I'm here to encourage and motivate you. What can I assist you with today?", "I'm your chatbot companion. How's your day going?"]),
    (r'bye|goodbye', ["Goodbye! Remember, I'm here whenever you need support on your journey.", "Take care! Keep working towards your 10k goal."]),
    (r'can you help me?', ["Absolutely! I'm here to help you with any questions or challenges you have. What's on your mind?", "I'm here to support you. How can I assist you today?"]),
    (r'I am not feeling good', ["I'm sorry to hear that. It's okay to have tough days. What's been bothering you?", "I understand. Sharing can help. What's on your mind?"]),
    (r'i need motivation', ['Sure, here is a motivational quote:'] + motivational_quotes),
    (r'(.*)', ["I'm here to listen and support you. Feel free to share your thoughts and feelings.", "Please feel free to talk to me. I'm here for you."]),
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

# Main interaction loop
print("Hello! I'm your chatbot companion. You can type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Remember, I'm here to support your 10k journey.")
        break
    response = chatbot.respond(user_input)
    if isinstance(response, list):
        response = random.choice(response)
    print("Chatbot:", response)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def behavior_change_chatbot():
    user_input = request.json.get('user_input')
    # Your chatbot logic to generate a response based on user_input
    response = chatbot.respond(user_input)
    if isinstance(response, list):
        response = random.choice(response)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)