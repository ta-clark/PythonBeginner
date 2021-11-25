import math

# Ask for three numbers in degrees
first = int(input('Enter First Number in Degrees: '))
second = int(input('Enter Second Number in Degrees: '))
third = int(input('Enter Third Number in Degrees: '))

# Compute user inputs from degrees to radians and display it

radian1 = math.radians(first)
radian2 = math.radians(second)
radian3 = math.radians(third)

print('First Radian: ',radian1, '\nSecond Radian: ', radian2, '\nThird Radian: ',radian3)

# Show smallest of the three inputs and display it
smaller = min(radian1, radian2, radian3)
print('Smallest Radian = ',smaller)

# Show largest of the three inputs and display it
largest = max(radian1, radian2, radian3)
print('Largest Radian = ',largest)


