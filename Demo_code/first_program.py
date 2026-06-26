# Print Hello World
print("Hello World")

# Create a variable to store my first name
first_name = "Zackery"

# Create a variable to store my last name
last_name = "Hunter"

# Write a Python statement to display "My full name is Zack Hunter"
print("My full name is", first_name, last_name, sep=" ")

#Print using the f string (String Interpolation)
print(f"My full name is {first_name} {last_name}.")

# Create a variable to store my age and weight
age = 16
weight = 115
half_age = age / 2

# Print a sentence with name, age, and weight
print(f"My name is {first_name} {last_name}.\nI am {age} years old, and my weight is {weight} lbs.")

# Get and print the data type for age, weight, and half age
print("\nChecking data types\n")
print(type(age))
print(type(weight))
print(type(half_age))

# Write three statements using string interpolation (f string) to print descriptive sentences for the data types.
print("\nChecking data types and listing corresponding variables\n")
print(f"Age is an {type(age)}")
print(f"Half Age is an {type(half_age)}")
print(f"Weight is an {type(weight)}")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"{number_1} + {number_2} = {total}")