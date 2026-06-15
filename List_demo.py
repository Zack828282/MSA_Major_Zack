def main():
    # Create a list of strings, integers, and different calues
    Names = ["John", "Mary", "Alice", "Bob"]
    List_of_integers = [10, 16, 24, 42, 14, 9]
    Random_type_list = ["Cyd", 15, 22,3, True, "Frank"]
    Empty_list = []

    # Print a list
    print(List_of_integers)

    # Add values to a list
    print("\nAdding values to a list\n---------------")
    Names.append("Johnny")
    List_of_integers.append(63)
    List_of_integers.append(5)
    print(f"Liat of Integers: {List_of_integers}\n")
    print(f"List of names: {Names}\n")
    

    print("\nGet the number of items in a list\n---------------")
    print(f"\nItems in Integer list {len(List_of_integers)}\n")

    print ("Get values at specifical indices in a list\n-----------------")
    print(f"\nFirst item in names list: {Names[0]}\n")

    # Print all ites in a list
    print(f"\nPrinting all names\n-------------")
    for Name in Names:
        print(Name)

    print("\nPrinting all names with ine values\n-----------------")
    for index in range (len(Names)):
        print(f"Name[{index}] = {Names[index]}")

    # Calculate the sum of all the integers in a list
    Sum_of_all_integers = 0
    for number in List_of_integers:
        Sum_of_all_integers += number

    print(f"Sum of all integers: {Sum_of_all_integers}")

    # Calculae the average of all integers in list
    Integer_avg = Sum_of_all_integers / len(List_of_integers)
    print(f"Average of all integers: {Integer_avg}")

    # Does the list contain a specific item
    Search_name = "Veronica"
    if Search_name not in Names:
        print(f"{Search_name} is not in the names list")
    else:
        print(f"{Search_name} is in the names list")

    # Find the largest value in a list
    # Set Max_value to the first value in the list
    Max_value = List_of_integers[0]

    # Loop over the entire list
    for Current_value in List_of_integers:
        # If Current_value > Max_value, set max to current
        if Current_value > Max_value:
            Max_value = Current_value
    # when the loop ends, print the argest number
    print(f"List of integers: {List_of_integers}")
    print(f"The largest value in the list of integers is: {Max_value}")
main()