# Create A McdoBot
# Author: Shaun
# 21 February 2024 

answer = input("Would you like fries with your meal? (Yes/No) ")

if answer.strip(" !.?,").lower() == "yes":
    print("Here's your meal with fries!")
elif answer.strip(" !.?,").lower() == "no":
    print("Here's your meal without fries!")
else:
    print(f"Sorry. I don't understand {answer}.") 