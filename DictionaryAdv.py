import random

#Sample response
chatbot_responses = {
    "greetings":["Hello","hi there!","Greetings!!","Hey!!"],
    "goodbye":["Good bye!","See you later.","Take Care!"],
    "thanks":["You are welcome!","Glad to hear!","No Problem!"],
    "How are you":["I'm just a bot!","I'm fine, Thanks for asking"]
}

#user input
bot_input = input("You: ").lower()

#Check for best match
response = None
for key,responses in chatbot_responses.items():
    if any(word in bot_input for word in key.split()):
        response = random.choice(responses)
        break
    
if response:
    print("Bot: ",response)
else:
    print("I'm not sure how to respond to that")