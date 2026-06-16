# Define main
def main():
        # Create a variable for the starting cost OUTSIDE OF THE WHILE LOOP
        Initial_total = 0
        # Create the dictionary that wlll store all of the menu items and their costs
        Menu = {"Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50, "Super burrito": 8.50, "Super quesadilla": 9.50, "Taco": 3.00, "Tortilla salad": 8.00,}
        # Start a while loop
        while (True):
        # Prompt the user to input an item that is on the menu
            User_input = input("\nItem:\n")
        # If the user inputs end, break the loop, no matter the case
            if User_input.capitalize() == "End":
                break
        # If the item that the user inputs is invalid, restart the loop without an error message
            elif User_input.capitalize() not in Menu.keys():
                continue
            else:
                for Item in [Menu]:
                    Initial_total += Menu[User_input.capitalize()]
                    print(f"Total: ${Initial_total:.2f}")
                    continue
        # If the user enters a valid menu item, call upon the dictonary to find its value, add it to the variable used to store total, print the total, and continue the loop
    # Run main
main()