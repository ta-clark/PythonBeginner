# Ask for width and length in feet
width = float(input('Enter Width of Carpet in Feet: '))
length = float(input('Enter Length of Carpet in Feet: '))

# Ask for quality of carpet (three grades: fair, good, excellent)
qual = str(input('Would you like fair, good, or excellent quality of carpet? '))

# fair costs 2$ per square foot
# good costs $4 per square foot
# excellent costs $8 per square foot

# Define function to output price based on length, width, quality

def cost(L, W, qual):
    if qual == 'fair':
        price = 2 * (L * W)
        return price
    elif qual == 'good':
        price = 4 * (L * W)
        return price
    elif qual == 'excellent':
        price = 8 * (L * W)
        return price
    else:
        print('Invalid. Please try again.')
    
# Display the cost of carpeting

print(cost(length, width, qual))
