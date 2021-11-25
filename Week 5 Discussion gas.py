# This program asks the user what is the current national average gas price
# Assign the national average gas price to the variable 'gas'

gas = '3.41'

# Create a while loop that prompts user input 

while True:
    answer = input("What is the current national average gas price as of 11/16/2021? Example: 1.50 ")
    if answer != gas:
        print("Incorrect.")
    elif answer == gas:
        break
    
print("That is correct! The national average gas price as of 11/16/2021 is", answer)
