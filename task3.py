import random

class SimpleChatbot:
    def __init__(self):
        self.greetings = ["hello", "hi", "hey", "howdy"]
        self.responses = {
            "how are you": ["I'm just a bunch of code, but I'm doing well!", "I'm here to help you!", "Doing great, thanks for asking!"],
            "what's your name": ["I'm a simple chatbot without a name!", "You can call me Chatbot.", "I'm just your friendly assistant!"],
            "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", 
                               "Why did the scarecrow win an award? Because he was outstanding in his field!"],
            "default": ["I'm not sure how to respond to that. Can you ask something else?"]
        }

    def respond(self, user_input):
        user_input = user_input.lower()
        
        if user_input in self.greetings:
            return random.choice(["Hello!", "Hi there!", "Greetings!"])
        
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        
        return random.choice(self.responses["default"])

def chat():
    chatbot = SimpleChatbot()
    print("Welcome to the chatbot! Type 'quit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
