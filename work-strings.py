# Designing Algorithms
# Author: Shaun Mundie
# Date: 9 February 2024

# 1. Greet the user 
print("Hello, user!") 
print()
# Put a space

# 2. Ask them a question 
print("How is your day going so far?")
print()

input()
print()
# Put another space

# 3. Respond specifically to that question 
print("Wow. Thanks for sharing.")

# 4. Ask for the user's name 
#     - store the user's response
#     - use the person's name in a reply
print()
print("So, what's your name?")
print()

user_name = input()
print()

print(f"It's really nice to meet you {user_name}!") 
print() 

print(f"What's your favourite colour {user_name}?") 
print()

colour = input() 
print()

print(f"The colour {colour} is awesome!") 
print()

print("I have one last question!") 
print()

print("What is your favourite food?")
print()

food = input() 
print()

print(f"Yum! I love {food}!")
print()

# 5. Say goodbye 
print(f"Alright, Goodbye {user_name}!") 