
""""""""
# Returns list of student objects
# Input: None
# Output: List of students with data

""""""""


from Student import Student
def load_students(): 
     co_data_num = 0
     student_list: list[Student] = []
     student_thing = open("students.csv", "r")
     for line_of_data in (student_thing):
          if co_data_num == 0:
                co_data_num += 1
                continue
          info = line_of_data.split(",")
          try:
               if len(info) != 6:
                    co_data_num += 0
               #print("There's an error somewhere in this data! (Length of lists related)")

          except:
               co_data_num += 0
               break
            
          first_name = info[0]
          last_name = info[1]
          major = info[2]
          credit_hours = info[3]
          gpa = info[4]
          id = info[5]
          try:
                 credit_hours = int(info[3])
                 gpa = float(info[4])
          except:
                 # Print("There's an error somewhere in this data! (Credit hour and/or gpa related)")
                 break
          induvidual = Student(info[0], info[1], info[2], info[3], info[4], info[5],)
          student_list.append(induvidual)
     #print(student_list)
     return student_list

""""""
# Function to convert student objects into student dictionaries
# input: List of student objects
# Output: List of student dictionaries
""""""
def student_to_dictionary(student_list: list[Student]) -> list[dict]:
# Create an empty list to store dictionaries

     student_dictionary_list = []
     # Loop through the list and write each student's data to a dictionary
     for student in student_list:
          # Create an empty dictionary
          student_dictionary = {}
          # Make entries into the dictionary using the student properties
          # First name, last name, major, gpa, class, id
          student_dictionary["first_name"] = student.get_first_name()
          student_dictionary["last_name"] = student.get_last_name()
          student_dictionary["major"] = student.get_major()
          student_dictionary["gpa"] = student.get_gpa()
          student_dictionary["credit_hours"] = student.get_credit_hours()
          student_dictionary["id"] = student.get_ID()
          # Append the dictionary to the list of dictionaries
     
          student_dictionary_list.append(student_dictionary)
     # Return the list of dictionaries
     return student_dictionary_list

     
""""""


""""""""
# Returns list of student objects
# Input: None
# Output: List of students with data

""""""""

def get_student_dictionaries():
     # get a list of students
     student_list = load_students()

     # get a list of student dictionaries
     student_dictionaries = student_to_dictionary(student_list)

     return student_dictionaries

get_student_dictionaries()