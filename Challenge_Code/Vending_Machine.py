# Define/open a main function that will run important code
def main():
    # In main, start a while loop
    while (True):
        try:
            # Create the variable that will be used for storing initial amount due (Initial_amount_due)
            Initial_amount_due == 50
            # Create a variable for what coin is entered/Start with a try with int(prompt(... that prompts the user to insert a coin
            coin_inserted = int(input("Please insert a coin:   "))
            if coin_inserted == 1:
                New_amount_due == 50 - coin_inserted
                print(New_amount_due)
            
        except:
            print("Please enter a valid coin value")
            # Print title
            # Print Initial
            # Start with a try with int(prompt(... that prompts the user to insert a coin
            # Write if/elif statements that check for correct denomination, 
            # Subtract the correct amount from Initial_amount_due
            # Call upon the newly obtained number, and reprompt the user
            # Continue looping until condition of line 11 is met
            # If remaining balance becomes <= 0, multiply it by -1, and display it as change owed if it was previously a negative number
            # break loop after no more money is due
            # Write an except statement that continues the loop/prompting for cases where input isn't valid
            # Run main
            main()