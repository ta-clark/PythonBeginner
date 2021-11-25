# This is a Compound Interest Calculator that will tell a user what their investment value will be based on the information given
print("Compound Interest Calculator")

# User is prompted for their initial investment information
savings = float(input("Initial Savings: "))
years = float(input("Duration of investment in years: "))
ARR = float(input("Annual Return Rate (Enter 7 for 7%): "))
compound_frequency = float(input("Number of times interest is compounded per year (Standard is 1): "))

# If the user has a return rate less than 5%, they are notified that they are barely beating inflation
if ARR < 5:
    print("Your annual return rate is less than recommended. The average US stock market return rate per year is 8.29 after adjusted for inflation")
    
# Program computes the final value of their investment and displays it for the user
money = savings*(((1+(ARR/(100)/compound_frequency))**(compound_frequency * years)))
print("Investment value: ", money)


