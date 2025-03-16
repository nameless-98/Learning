#read data
def load_response(filename):
    responses = {}
    with open(filename,"r") as file:
        for line in file:
            key , value = line.strip().split("=")
            responses[key]=value
    return responses

chatbot_responses = load_response("chat_history.txt")

user_input = input("You: ").lower()
response = chatbot_responses.get(user_input,"I don't understand")

print("Bot: ",response)