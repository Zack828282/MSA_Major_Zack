# Define Difficulty_obtainer
import random
def Difficulty_obtainer():
    # Start a while loop
    while (True):
        # Prompt user for input
        # Accept and store input if it is valid
        try:
            Difficulty = int(input("Please choose a difficulty (1, 2, or 3): "))
            if Difficulty > 0 and Difficulty < 4:
                break
            else:
                print("Please enter a valid number\n")
                continue
        except:
            print("Please enter an integer for difficulty\n")
    return Difficulty
    
    
# Define Question_number_obtainer
def Question_number_obtainer():
# Start a while loop
    while (True):
        # Prompt user for input
        # Accept and store input if it is valid
        try:
            Question_number = int(input("\nPlease choose the number of problems (3 - 10): "))
            if Question_number > 2 and Question_number < 11:
                break
            else:
                print("Please enter a valid number\n")
                continue
        except:
            print("Please enter an integer for difficulty\n")
    return Question_number
def Randgen_dif_1():
    random_generator = random.Random()
    random_number_1 = random_generator.randint(1,9)
    random_number_2 = random_generator.randint(1,9)
    return random_number_1 and random_number_2
def Randgen_dif_2():
    random_generator = random.Random()
    random_number_1 = random_generator.randint(10,99) 
    random_number_2 = random_generator.randint(10,99)
    return random_number_1 and random_number_2
def Randgen_dif_3():
    random_generator = random.Random()
    random_number_1 = random_generator.randint(100,999)
    random_number_2 = random_generator.randint(100,999)
    return random_number_1 and random_number_2
# Define main
def main():
        Correct_answers = 0
        Incorrect_answers = 0
        Total_answers = 0
        # Take difficulty from Difficulty_obtainer
        Difficulty = Difficulty_obtainer()
        # Take question number from Question_number_obtainer
        Question_number = Question_number_obtainer()
        # Start a for loop with a length based on output of Question_number_obtainer
        for Questions in range (Question_number):        
            if Difficulty == 1:
                random_number_1 = Randgen_dif_1()
                random_number_2 = Randgen_dif_1()
            elif Difficulty == 2:
                random_number_1 = Randgen_dif_2()
                random_number_2 = Randgen_dif_2()
            elif Difficulty == 3:
                random_number_1 = Randgen_dif_3()
                random_number_2 = Randgen_dif_3()
            for Questions in range (3):
                # Use if statements to generate two random numbers of certain lengths based on output of difficulty obtainer
                    # Create a random number generator Sum = random_number_1 + random_number_2
                    try:
                        User_input = int(input(f"\n{random_number_1} + {random_number_2} = "))
                        Sum = random_number_1 + random_number_2
                        if User_input == Sum:
                            print("\nCorrect!")
                            Correct_answers += 1
                            Total_answers += 1
                            break
                        else:
                            print("\nWrong!\n")
                            if Questions == 1 or 0:
                                continue
                            elif Questions == 2:
                                print(f"Correct answer: {random_number_1} + {random_number_2} = {Sum}\n")
                                Incorrect_answers = Incorrect_answers + 1
                                Total_answers = Total_answers + 1
                                break    
                    except:
                        print("\nWrong!\n")
                        if Questions == 0 or 1:
                                continue
                        elif Questions == 2:
                                print(f"Correct answer: {random_number_1} + {random_number_2} = {Sum}\n")
                                Incorrect_answers = Incorrect_answers + 1
                                Total_answers = Total_answers + 1
                                break
                
            continue
        print(f"Questions answered correctly: {Correct_answers} / {Total_answers}")
        Ratio_helper = Correct_answers * 100
        Percent = Ratio_helper / Total_answers
        print(f"Percent correct: {Percent:.2f}%")
        
        
            # Ask for an input for a question formatted randint_1 + randint_2 = (INPUT), and store input as a variable
            # Do math to figure out what the sum of the two random ints actually equal, and make that result a variable
            # start a for loop to loop the same question 3 times if needed, and store how many times it's been done
                # Check whether or not User_input and Sum are the same, and return either TRUE or FALSE
                # Use if statements to print Correct or Wrong depending on whether or not TRUE or FALSE was returned,
                # If TRUE, print correct, and break the for loop
                # If FALSE, allow the loop to continue
                # if stored variable for the for loop is 4, print the sum of the two randints, and allow the for loop to stop
        # allow the bigger for loop to end and make sure no more code is ran
main()