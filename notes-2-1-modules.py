# Lists and Modules
# Author: Shaun
# 8 March 2024

import random 

def coin_flip():
    # Returns heads or tails or other?
    # Heads is any number from 0 to 0.499999999
    # Tails is any number from 0.5 to 0.999999
    # Other is any number greater than 0.999999
    roll = random.random()

    if roll <= 0.5:
        return "heads"
    elif roll < 0.999999:
        return "tails"
    else:
        return "other?"
    
    
def main():
    # Keep track of heads and tails
    heads = 0
    tails = 0

    for _ in range(100):
        if result == "heads":
            heads = heads = 1 # increment
        elif result == "tails":
            tails =+ 1        # increment
        else: other = 0

# Print Results

main()