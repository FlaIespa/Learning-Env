from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot("MentalHealthBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train("chatterbot.corpus.english")

# Define a function for user interaction
def chat_with_bot():
    print("MentalHealthBot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("MentalHealthBot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("MentalHealthBot:", response)

if __name__ == "__main__":
    chat_with_bot()
