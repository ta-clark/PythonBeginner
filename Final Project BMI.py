# Name of six individuals
print("Please enter the names of the 6 users who want to calculate thier BMI, one at a time: ")
individuals = []
bmi_list = []

# For loop and range of the six individuals
for i in range(0, 6):
    user = input()
    individuals.append(user)

# Define BMI in height & weight. Define formula for BMI
def BMI(height, weight):
    bmi = (weight * 703) / (height ** 2)
    return bmi

# Define the BMI categories 
def bmi_result(bmi) :
    if 18.5 > bmi:
       print("You are underweight.")
    elif 18.5 <= bmi < 25:
       print("Your weight is normal.")
    elif bmi >= 25 and bmi < 30:
       print("You are overweight.")
    elif bmi >= 30:
        print("You are obese.")

# Prompt individuals for their BMI data and display the results for each individual
for individual in individuals:
    print(individual+", Please enter your height and weight")
    height = float(input("Enter height in inches:  "))
    weight = float(input("Enter weight in pounds:  "))
    bmi = BMI(height, weight)
    bmi_result(bmi)
    print("The body mass index for", individual, "is:  ", (round(bmi, 2)))
    bmi_list.append(bmi)

print("The BMI results of all six individuals are: ", bmi_list)

# Thresholds for BMI categorization
underweight_threshold = 18.5
normal_threshold = 25
obese_threshold = 30

# Number of individuals in each category
underweight_individuals = [bmi for bmi in bmi_list if bmi < underweight_threshold ]
normal_individuals = [bmi for bmi in bmi_list if bmi > underweight_threshold  and bmi < normal_threshold]
overweight_individuals = [bmi for bmi in bmi_list if bmi >= normal_threshold and bmi < obese_threshold]
obese_individuals = [bmi for bmi in bmi_list if bmi > obese_threshold]

# Display the number of individuals in each BMI category 
print(f"The number of underweight individuals is {len(underweight_individuals)}.")
print(f"The number of normal individuals is {len(normal_individuals)}.")
print(f"The number of overweight individuals is {len(overweight_individuals)}.")
print(f"The number of obese individuals is {len(obese_individuals)}.")

