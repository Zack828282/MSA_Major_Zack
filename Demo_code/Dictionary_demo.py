def main():
    # The need for dictionaries
    Scores = [55, 75, 87, 82, 91]
    Students = ["Alice", "Bob", "Jerry", "Jane", "Bill"]

    # Print the name of the students with their scores
    print("Students and scores using the lsits\n--------------")
    for index in range (len(Scores)):
        print(f"{Students[index]} = {Scores[index]}%")

    
    # Create a dictionary of nams and scores
    Student_scores = {
        'Alice': 55,
        "Bob": 75,
        "Jerry": 87,
        "Jane": 82,
        "Bill": 91,
    }


    # Print Bob and Jane's scores
    print("Print Bob and Jane's scores\n--------------")
    print(Student_scores["Bob"])
    print(Student_scores["Jane"])

    # print all the data in the student scores dictionary
    print("\nPrint all student score data from the dictinary:\n----------------------")
    for Student in Student_scores:
        print(f"{Student}: {Student_scores[Student]}")

        # Create a dictionary to store car information
        # Make, model, year, value and engine size
        Car_info = {
            "Make": "Ferrari",
            "Model": "F-50",
            "Year": 2024,
            "Value": 500000,
            "Engine_size": 2.4
        }
        print("\nGet all car information\n----------------")

        #for Key, Value in [Car_info]:
        #print(f"{Key}: {Value}")
            
            # I spent a lot of time trying to fix the code above, enough to were I wasn't able to keep up and do what was done next, so here's a rundown:
            # You can have two dictionaries, both stored in a list
            # If you want to print some of both, do a loop in a loop. Ill try to do that below
            # Don't trust this code. I don't know why it's all wrong, but something's off, and I'm not able to spend time fixing it right now.
        Car_info_2 = {
            "Make": "Lamborghini",
            "Model": "Sesto elemento",
            "Year": 2022,
            "Value": 750000,
            "Engine_size": 2.4
        }
        Car_info["transmission"] = "manual"
        Car_info_2["transmission"] = "automatic"
        dictionary_list = [Car_info, Car_info_2]
        for feature in dictionary_list:
                print("\nCar information\n-------------------")
                for feature, value in dictionary_list:
                    print(f"{feature}: {value}")
        
            # It prints the stuff twice, but honestly I can deal with that. At least this runs.
            # You can also have dictionaries of dictionaries, where you can put, say, the car name, and then the cooresponding dictionary (Ferrari: Car_info)
            # You can call upon these nested dictionaries, which just prints out all the information in all of the layer 2 dicionaries that are in the layer 1 dictionary.
            # On keys that aren't in a dictionary, use: (if key not in dictionary.keys(): print(Key doesn't exist) else: do whatever is supposed to be done next)
            # Adding an entry to a dictionary

main()