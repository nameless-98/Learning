greetings = ("hello","hi","greetings","bro","hey")

user_input = input("You: ").lower()

res = 0
for greeting in greetings:
    if greeting in user_input:
        print("hi there")
        res += 1
    else:
        continue
if(res==0):
    print("I don't get it")