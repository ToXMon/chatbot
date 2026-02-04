#!/usr/bin/env python3
"""A simple, friendly chat bot that loves to chat!"""

import random
import datetime

class ChatBot:
    def __init__(self, name="VibeBot"):
        self.name = name
        self.responses = {
            "greeting": [
                "Hey there! 👋 I'm {name}, ready to chat!",
                "Hello! How can I help you vibe today?",
                "Hi! I'm {name}, let's talk!"
            ],
            "how_are_you": [
                "I'm doing great, thanks for asking! 😊",
                "Living the bot life! How about you?",
                "Awesome! Every conversation is a new adventure!"
            ],
            "joke": [
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
                "Why did the bot go on a diet? Too many cookies! 🍪",
                "What's a bot's favorite music? Heavy metal! 🎸"
            ],
            "default": [
                "That's interesting! Tell me more!",
                "I see! What else is on your mind?",
                "Cool! I'd love to hear more about that.",
                "Fascinating! Any other thoughts?"
            ]
        }
    
    def get_response(self, user_input):
        """Generate a response based on user input."""
        user_input = user_input.lower()
        
        # Greetings
        if any(word in user_input for word in ["hi", "hello", "hey", "greetings"]):
            return random.choice(self.responses["greeting"]).format(name=self.name)
        
        # How are you
        if any(phrase in user_input for phrase in ["how are you", "how's it going", "how do you feel"]):
            return random.choice(self.responses["how_are_you"])
        
        # Jokes
        if any(word in user_input for word in ["joke", "funny", "laugh"]):
            return random.choice(self.responses["joke"])
        
        # Time
        if "time" in user_input:
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')} ⏰"
        
        # Default response
        return random.choice(self.responses["default"])
    
    def chat(self):
        """Start an interactive chat session."""
        print(f"\n{'='*50}")
        print(f"🤖 {self.name} is online!")
        print(f"{'='*50}")
        print("Type 'quit', 'exit', or 'bye' to end the chat.\n")
        
        # Initial greeting
        print(f"{self.name}: {random.choice(self.responses['greeting']).format(name=self.name)}")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ["quit", "exit", "bye"]:
                    print(f"\n{self.name}: Goodbye! Come back and chat anytime! 👋\n")
                    break
                
                if not user_input:
                    continue
                
                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! 👋\n")
                break


def main():
    bot = ChatBot()
    bot.chat()


if __name__ == "__main__":
    main()
