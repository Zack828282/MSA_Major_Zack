# I acidentally improved the code in here, so it's the same as in the improved file.
# Program to convert pounds (lbs) to kilograms (kg)
# INPUT (getting data that willb e processed)
# Loop
while (True):
    # Validate input: ensure the data is numerical
    try:
         # Prompt user to enter weight in pounds
        user_weight = float(input("Enter weight in pounds: "))
        break
    except:
        print("ERROR: Please enter a number")
        continue
    # If the input is invalid, then reprompt the user until the give input is valid

# PROCESSING (process the data in some way)
# Use a conversion factor to convert pounds to kilograms (2.205 lbs = 1 kg)
lbs_to_kg = 2.205
user_weight_in_kg = user_weight / lbs_to_kg

# OUTPUT (Show the user the result)
# Print the output to the user
print(f"You weigh {user_weight_in_kg:.2f} kg.")
