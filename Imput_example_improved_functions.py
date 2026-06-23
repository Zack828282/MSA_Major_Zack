# Program to convert pounds (lbs) to kilograms (kg)
# INPUT (getting data that willb e processed)
def get_positive_float_input():
        #Loop 
        while (True):
            # Validate input: ensure the data is numerical
            try:
                # Prompt user to enter weight in pounds
                user_weight = float(input("Enter weight in pounds: \n"))
                # Check if weight is less than or equal to 0, and if it is, run error message, and try again
                if user_weight <= 0:
                    print("ERROR: Enter a number greater than 0\n")
                    continue
                break
            except:
                print("ERROR: Please enter a number.\n")
                continue
        # If the input is invalid, then reprompt the user until the give input is valid
        return user_weight

def main():
    # Input
    user_weight = get_positive_float_input()
    # PROCESSING (process the data in some way)
    # Use a conversion factor to convert pounds to kilograms (2.205 lbs = 1 kg)
    lbs_to_kg = 2.205
    user_weight_in_kg = user_weight / lbs_to_kg

    # OUTPUT (Show the user the result)
    # Print the output to the user
    print(f"You weigh {user_weight_in_kg:.2f} kg.")
main()