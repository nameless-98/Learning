import random

#sample response
responses = {
    "greetings":["Hello","hi there!","Greetings!!","Hey!!"],
    "goodbye":["Good bye!","See you later.","Take Care!"],
    "thanks":["You are welcome!","Glad to hear!","No Problem!"],
    "How are you":["I'm just a bot!!","Pretty much good."]
}

#Take response
user_input = input("You: ",).lower()

#logic to Give response
if user_input in ["hi","hello","hey"]:
    print("Bot: ",random.choice(responses["greetings"]))
elif user_input in ["bye","goodbye"]:
    print("Bot: ",random.choice(responses["goodbye"]))
elif user_input in ["how are you","what about you"]:
    print("Bot: ",random.choice(responses["How are you"]))
else:
    print("Bot: ",random.choice(responses["thanks"]))