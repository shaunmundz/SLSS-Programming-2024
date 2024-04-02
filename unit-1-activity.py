# Doctor Bot
# Author: Shaun Mundie
# 4 March 2024

def greet(name):
    print("Hello, " + name + "!")

greet("Patient") 

print("Before we start, can you confirm your name? ")

user_name = input() 

answer = input(f"Okay {user_name}. I heard that you are experiencing back pain, is that correct? (yes/no) ")

if answer.strip(" !.?,").lower() == "yes":
    print("Alright! Visit back in two days and your prescription will be ready for you.")
elif answer.strip(" !.?,").lower() == "no":
    print("Great, get out.")
else:
    print(f"Sorry. I don't understand what {answer} is.") 

def pain(num):
    if num == 0:
        return "You gotta be joking."
    if num == 1:
        return "Seriously?"
    if num == 2:
        return "Ain't no way."
    if num == 3:
        return "That's crazy."
    if num == 4:
        return "Wow."
    if num == 5:
        return "Alright"
    if num == 6:
        return "Gotcha"
    if num == 7: 
        return "Thanks!"
    if num == 8: 
        return "Appreciate it!" 
    if num == 9:
        return "Happy to help!"
    if num == 10:
        return "Woohoo!🎉"

user_input = input("Please rate your experience from (1-10) ")

user_number = int(user_input)

result = pain(user_number)

print(result)

print(f"Goodbye {user_name}!")