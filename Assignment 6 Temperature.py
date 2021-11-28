# Opening message
print("This program converts the recorded temperature of 10 days in Celsius to Fahrenheit for you.")

# List temperatures in celsius
temperatures_in_celsius = []

# Range of temperatures in celsius, have user input temperatures for days 1-10
for i in range(1, 11): temperatures_in_celsius.append(float(input(f"Enter the temperature for day {i}: ")))

# Return the temperatures in Celsius
print("\nThe temperatures in Celsius are")

print(temperatures_in_celsius)

# Calculate temperatures from celsius to fahrenheit and print 
temperatures_in_fahrenheit = [(temp * 1.8) + 32 for temp in temperatures_in_celsius]

print("\nThe temperatures in Fahrenheit are")

print(temperatures_in_fahrenheit)

# Define the threshold for cool, warm and hot days and how it is computed
cool_threshold = 60
warm_threshold = 85

cool_days = [temp for temp in temperatures_in_fahrenheit if temp < cool_threshold]
warm_days = [temp for temp in temperatures_in_fahrenheit if temp >= cool_threshold and temp < warm_threshold]
hot_days = [temp for temp in temperatures_in_fahrenheit if temp >= warm_threshold]

# Print the final result 
print(f"The number of cool days is {len(cool_days)}.")
print(f"The number of warm days is {len(warm_days)}.")
print(f"The number of hot days is {len(hot_days)}.")

