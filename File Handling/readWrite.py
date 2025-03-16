#Saving conversation
def save_conversation(user,bot):
    with open("chat_history.txt","a") as file:
        file.write(f"You: {user}\n")
        file.write(f"Bot: {bot}\n")
        file.write("-" * 30 + "\n")
        
chatbot_response = {
    "hello" : "Hi how can I help you?",
    "how are you" : "I'm doing great",
    "bye":"Goodbye! Have a nice day"
}     

user_input = input("You: ").lower()
response = chatbot_response.get(user_input,"I don't understand")

print("Bot: ",response)
save_conversation(user_input,response)