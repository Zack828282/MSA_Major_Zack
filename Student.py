class Student():
    # Define a cunstructor
    # The constructor is a function that is called to create a student
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id):
        # Define class properties with the parameter values
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__ID = id

    # Create getter and setter methods for class properties
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name
        return new_first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name
        return new_last_name
    
    def get_major(self):
        return self.__major
    
    def set_major(self, new_major):
        self.__major = new_major
        return new_major
    
    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_credit_hours(self, new_credit_hours):
        self.__credit_hours = new_credit_hours
        return new_credit_hours
    
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa
        return new_gpa
    
    def get_ID(self):
        return self.__id

    def get_class_level(self):

        class_level = "Placeholder"

        if int(self.__credit_hours) < 31:
            class_level == "Freshman"
        elif int(self.__credit_hours) > 30 and int(self.__credit_hours) < 61:
            class_level == "Sophomore"
        elif int(self.__credit_hours) > 60 and int(self.__credit_hours) < 91:
            class_level == "Junior"
        elif int(self.__credit_hours) > 90:
            class_level == "Senior"
        return class_level

    def update_credit_hours(self, additional_credit_hours):
        self.__credit_hours += additional_credit_hours
        return
    

    # Create a method to print automobile data
    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Credit hours: {self.__credit_hours}, Major: {self.__major}")
        print(f"GPA: {self.__gpa}, ID: {self.__ID}")