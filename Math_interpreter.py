# While loop
while (True):
    # INPUT
    # Prompt user to enter 2 numbers and an operator
    Input_expression = input("Please enter a expression in form X Y Z, where X and Z are integers, and Y is an operand (EX: 2 * 5, 3 / 4):")

    # PROCESS
    # Validate expression format
        # Use the split() method to splt the expression at the space " "
    Input_split = Input_expression.split(" ")

        # If the length of the resulting list is not 3, then invalid format
    if len(Input_split) != 3:
        print("Please enter the expression with valid formatting")
        continue
    else:
         X = Input_split[0]
         Y = Input_split[1]
         Z = Input_split[2]
    
    # Validate that X and Z are integers
        # Convert to int
        # If conversion  causes exception, then invalid format
    try:
        int(X) + int(Z)

    except:
        print("Please enter numerical values for both X and Z")
        continue
    
    # Validate that Y is an acceptable operator (+, -, *, /,)
    # Use an if statement to determine if Y == + or - or * or /
    # Invalid format if not
    if Y != "+" or "-" or "*" or "/":
        print('Please enter a valid operator (+, -, *, or /) for your Y value')
        continue
    # Validate that when Y is /, Z is not 0
    # Use an if statement of Y ==/ and Z == 0, Invalid format: Divide by 0 error
    if Y == "/" and Z == 0:
        print("ERROR: Cannot divide by 0")
    
    # Do the correct math

    if Y == "/":
    
    if Y == "/":

    if Y == "/":

    if Y == "/":


    # OUTPUT
    # Print the output to the user