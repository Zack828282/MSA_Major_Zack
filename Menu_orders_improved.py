# Function loads data from a file and returns a dictionary
# Input: Whatever the filename happens t be
# Output: Dictionary
def load_menu_items(Filename:str) -> dict:
             # Open menu.txt: Create a file handler to open file in read mode
        data_file = open(Filename, "r")
        print(data_file)

        # Create an exmpty dictionary
        Menu_items = {}
        # Use a loop to read the contents of the file line by line
        for line_of_data in data_file:
            # Split the line at the comma
            item_name_and_price = line_of_data.split(",")
            # Get the item and price from the list
            Item_name = item_name_and_price[0]
            Item_price = float(item_name_and_price[1])
            # Create an entry in the dictionary for the item and price
            Menu_items[Item_name] = Item_price
        # Close the file
        data_file.close()

        # Return the dictionary of menu items
        return Menu_items


# Define main
def main():
        # Create a variable for the starting cost OUTSIDE OF THE WHILE LOOP
        Initial_total = 0
        # Create the dictionary that wlll store all of the menu items and their costs
        Menu_items = load_menu_items("Menu.txt")
        # Start a while loop
        while (True):
        # Prompt the user to input an item that is on the menu
            User_input = input("\nItem:\n")
        # If the user inputs end, break the loop, no matter the case
            if User_input.capitalize() == "End":
                break
        # If the item that the user inputs is invalid, restart the loop without an error message
            elif User_input.capitalize() not in Menu_items.keys():
                continue
            else:
                for Item in [Menu_items]:
                    Initial_total += Menu_items[User_input.capitalize()]
                    print(f"Total: ${Initial_total:.2f}")
                    continue
        # If the user enters a valid menu item, call upon the dictonary to find its value, add it to the variable used to store total, print the total, and continue the loop
    # Run main
main()