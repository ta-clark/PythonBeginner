# Prompt the customer for their age and if they are watching a 3D Movie

age_group = int(input("Enter age: "))
x = str(input("Is the movie in 3D? (Yes or No) "))

# 3D movie surcharge = $5

if x == "yes" or x == "Yes":
    movie = 5

elif x == "no" or x == "No":
    movie = 0

# Children are defined as age 0-17, price = $8
# Adults are defined as age 18-59, price = $10
# Seniors are defined as age = 60-140, price $9

if age_group > 0 and age_group < 18:
    price = 8 + movie
    print("Your ticket price is $",price)

elif age_group > 17 and age_group < 60:
    price = 10 + movie
    print("Your ticket price is $",price)

elif age_group > 59 and age_group < 140:
    price = 9 + movie
    print("Your ticket price is $",price)

# The total price for a ticket is dependent on the age of the customer and if
# they are watching a 3D Movie which has a $5 surcharge



