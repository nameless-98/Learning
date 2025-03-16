import random
import re

# Sample responses
chatbot_responses = {
    "greetings": ["Hello!", "Hi there!", "Greetings!!", "Hey!!"],
    "goodbye": ["Goodbye!", "See you later.", "Take care!"],
    "thanks": ["You're welcome!", "Glad to hear!", "No problem!"],
    "how are you": ["I'm just a bot!", "I'm fine, thanks for asking!"]
}

# User input
bot_input = input("You: ").lower()

# Remove punctuation & split into words
words_in_input = re.findall(r'\b\w+\b', bot_input)

# Check for best match
response = None

for key, responses in chatbot_responses.items():
    key_words = key.split()  # Split key into words
    if any(word in words_in_input for word in key_words):  # Check word by word
        response = random.choice(responses)
        break

# Output response
if response:
    print("Bot:", response)
else:
    print("I'm not sure how to respond to that.")
