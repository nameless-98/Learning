import random

#pick from these randomly
response = ["Hello, How are you brother?",
        "Hi there, How can I assist you??",
        "Greetings!! How can I help you?"
        ]

user_input = input("You : ")

#Give response randomly
bot_response = random.choice(response)

print("bot: ",bot_response)
