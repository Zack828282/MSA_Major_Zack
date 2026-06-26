from Student import Student
def main(): 
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
                      print("There's an error somewhere in this data! (Length of lists related)")
            except:
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
                 print("There's an error somewhere in this data! (Credit hour and/or gpa related)")
                 break
            induvidual = Student(info[0], info[1], info[2], info[3], info[4], info[5],)
            student_list.append(induvidual.print_student_data())
    print(student_list)

def update_credit_hours(self, additional_credit_hours):
    self.__credit_hours += additional_credit_hours
    return
main()

