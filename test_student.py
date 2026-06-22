from Student import Student


def main():
    # Create a student
    test_student = Student("Truman", "Tiger", "Mizzou Stuff", 1839, 4.5, "12345678")
    
    test_student.print_student_data()

    # Test the set data hours method
    test_student.set_credit_hours(55)
    test_student.print_student_data()

main()