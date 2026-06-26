# While loop
while (True):
    # INPUT
    # Prompt user to enter 2 numbers and an operator
    Input_expression = input("Please enter a expression in form X Y Z, where X and Z are integers, and Y is an operand (EX: 2 * 5, 3 / 4): ")

    # PROCESS
    # Validate expression format
        # Use the split() method to splt the expression at the space " "
    Input_split = Input_expression.split(" ")

        # If the length of the resulting list is not 3, then invalid format
    if len(Input_split) != 3:
        print("\nPlease enter the expression with valid formatting\n")
        continue

    try:     

        X = int(Input_split[0])
        Y = Input_split[1]
        Z = int(Input_split[2])
    
    # Validate that X and Z are integers
        # Convert to int
        # If conversion  causes exception, then invalid format

    except:
        print("\nPlease enter numerical values for both X and Z\n")
        continue
    
    # Validate that Y is an acceptable operator (+, -, *, /,)
    # Use an if statement to determine if Y == + or - or * or /
    # Invalid format if not
  
    
    
    # Validate that when Y is /, Z is not 0
    # Use an if statement of Y ==/ and Z == 0, Invalid format: Divide by 0 error
    
    # Do the correct math
    # OUTPUT
    # Print the output to the user
    if Y == "+":
        Final_result = float(X) + float(Z)
        print(f"{X} {Y} {Z} = {Final_result}")
    
    elif Y == "-":
        Final_result = float(X) - float(Z)
        print(f"{X} {Y} {Z} = {Final_result}")

    elif Y == "*":
        Final_result = float(X) * float(Z)
        print(f"{X} {Y} {Z} = {Final_result}")

    elif Y == "/":
        if Z == 0:
            print("You are a chud")
            continue
        Final_result = X / Z
        print(f"\n{X} {Y} {Z} = {Final_result}\n")
    
    else:
        print('Please enter a valid operator (+, -, *, or /) for your Y value\n')
        continue

    Continue_var = input("Do you want to continue? (Enter y to continue): ")
    if Continue_var.lower() == "y":
        continue
    else:
        break



    # OUTPUT
    # Print the output to the user