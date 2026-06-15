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
main()