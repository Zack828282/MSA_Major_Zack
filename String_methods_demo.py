def main():
        My_name = "zackery"
        Last_name = "hunter"

        # Capitalize a string
        print(f"My name capitalized: {My_name.capitalize()}\n")


        # Make a string UPPERCASE
        print(f"My name made UPPERCASE: {My_name.upper()}\n")


        # Make a string lowercase
        print(f"My name made lowercase: {My_name.lower()}\n")
        print(f"My full name is {My_name.capitalize()} {Last_name.capitalize()}\n")

        if My_name.capitalize() == "Zackery":
            print("The strings are equal\n")
        else:
              print("The strings are not equal")

        print("\nUsing the Startswith() method\n------------------")
        # Determine if a string starts wit a set of characters
        print(f"My name starts with a Z or z: {My_name.startswith("Z") or My_name.startswith("z")}\n")

        if(not (My_name.startswith("zack"))):
            print(f"You spelled {My_name} incorrectly")
        else:
            print(f"You spelled {My_name} correctly")
           

        # There is also endswith() (I didn't put any code down here, but understand that its effectively just startswith())

        # and find

        print("\nUsing the find() method\n------------------")
        # find the c in zack
        Search_letter = "c"
        Index_of_substring = My_name.find(Search_letter)
        if Index_of_substring != -1:
            print(f"\nThe {Search_letter} is at index {My_name.find(Search_letter)} in {My_name}\n")
        else:
             print(f"There is no {Search_letter} in {My_name}")

        print("\nLooping through a string\n---------------------\n")
        for letter in My_name:
            print(letter)

        print(f"{My_name} has {len(My_name)} letters")
        # Print letters in a string, as well as cooresponding indexes using a for loop
            
        print("\nSearch a string\n-------------\n")
        sentence = "I have a dog. My dog is cute. Do you want a dog?"

            # Write code that counts how many times "dog" shows up in thew sentence

            # this is, in a nutshell our desired code/result

            # sentence.find(dog) = 9
            # sentence.find(dog) = 16
            # sentence.find(dog) = 42
            # sentence.find(dog) = -1
            # Dogs = 3
        search_word = "dog"
        start_index = 0
        Number_of_dogs = 0

        while (True):
             # Start at the beginning of the string
             # Search for the occurence of the word dog, starting at index 0
             dog_index = sentence.find(search_word, start_index)
             
             if dog_index == -1:
                  break
             else:
                  # If we find dog, add 1 to some variable used to store the number of dogs we find
                  Number_of_dogs += 1
                  # Update the staring index by 1 when a dog is found
                  # Continue searching the string from the next index after te one where we just found a dog
                  start_index = dog_index + 1
             # Do this until we find no more dogs (find() returns -1)
        print(f"There are {Number_of_dogs} {search_word}(s) in the sentence")



main()