# Create a decision structure to determine the season
# Winter, Spring, Summer, Fall
# As the user to enter the number of the month, Month being somewhere between one and twelve
# Winter is months 12, 1, and 2
# Spring is months 3, 4, and 5
# Summer is months 6, 7 and 8
# Fall is months, 9, 10, and 11
# Output the season
# Promt: Enter month number: 11
# Output: It is Fall

# Define main

def main():

    # Ask the user to input the number of the month

    while (True):
        try:
            Month_number = int(input("What number cooresponds to the current month of the year? (1 = January, 2 = February, etc...)\n"))

            # Create a block of code the ifs, elifs, and else that decided what number is what month

            if Month_number >= 3 and Month_number <= 5:
                print(f"-----------------\nMonth {Month_number} is in Spring!")
                break
            elif Month_number >= 6 and Month_number <= 8:
                print(f"-----------------\nMonth {Month_number} is in Summer!")
                break
            elif Month_number >= 9 and Month_number <= 11:
                print(f"-----------------\nMonth {Month_number} is in Fall!")
                break
            elif (Month_number >= 1 and Month_number <= 2) or (Month_number == 12):
                print(f"-----------------\nMonth {Month_number} is in Winter!")
                break
            else:
                print("Please enter a valid Month value\n")
        except:
            print("Please enter a valid Month value\n")
        continue

    # Print out the result
main()