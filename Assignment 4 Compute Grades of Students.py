# This program averages the quiz grades of 5 students and displays the highest grade

# Name of students
students = ("William", "Shaun", "Mike", "Joel", "David")

# Create a list to place the grades in and then prompt user for their grade

grades = []

for student in students:
    print(student + ", enter your quiz grade.")
    grade = input("My grade is: ")
    grades.append(float(grade)) 

print("Results:", grades)

# Compute average grade of students and display it
average = sum(grades) / len(grades)
print("The average grade is:", average)

# Compute the highest grade and display it
highest = max(grades)
print("The highest grade is:", highest)
