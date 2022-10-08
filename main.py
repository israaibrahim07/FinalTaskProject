from courses import Course
from student import Student

courses_list = []
student_list = []
def get_students_list(students):
    for student in students:
        print(str(student.student_number) + "\t\t" + student.student_name + "\t\t" + student.student_class)
def get_course_list(courses):
    for course in courses:
        course.get_course_details()

def find_student(student_number, students):
    index = 0
    for i in students:
        if i.student_number == student_number:
            return index
        index += 1
    return -1

def find_course(course_name, courses):
    index = 0
    for i in courses:
        if i.course_name in course_name:
            return index
        index += 1
    return -1


def update(student_name, student_class,studentNum=None):
    i = find_student(student_number=studentNum, students=student_list)
    if i != -1:
        student_list[i].student_name = student_name
        student_list[i].student_class = student_class


while True:
    x = int(input("Select Choice:\n1.Add new Student \n2.Remove Students \n3.Edit Student\n4.Display all Students\n5.Create New Course\n6.Add Course to Student\n0.Exit"))
    if x == 1:
        student_name = input("Enter Student Name: ")
        student_class = None
        while True:
            student_class = input("Select Course class from A or B or C: ")
            if student_class in ["A", "B", "C"]:
                break

        student_id = len(student_list) + 1
        student = Student(student_id,student_name, student_class)
        student_list.append(student)
        print("Student saved successfully")

    elif x == 2:
        try:
            get_students_list(student_list)
            student_id = int(input("Enter Student id: "))
            index = find_student(student_id, student_list)
            if index == -1:
                print("Student not exist")
            else:
                # student_list.remove(student_list[index])
                student_list.pop(index)
                print("delete done successful")

            get_students_list(student_list)

        except:
            print("Error")
    elif x == 3:
        student_id = int(input("Enter Student id: "))
        index = find_student(student_id, student_list)
        if index == -1:
            print("user not exist")
        else:
            student_name = input("Enter Student Name: ")
            student_class = None
            while True:
                student_class = input("Select Course class from A or B or C: ")
                if student_class in ["A", "B", "C"]:
                    break
            # student = Student(student_name, student_class)
            updat_list = update(student_name = student_name, student_class = student_class, studentNum=student_id)

            get_students_list(student_list)
            print("Student Updated successfully")

    elif x == 4:
        get_students_list(student_list)

    elif x == 5:
        course_name = input("Enter Course Name: ")
        course_class = None
        while True:
            course_class = input("Select Course class from A or B or C: ")
            if course_class in ["A", "B", "C"]:
                break

        course_id = len(courses_list) + 1
        course = Course(course_id,course_name, course_class)
        courses_list.append(course)
        print("Course Created")

    elif x == 6:
        try:
            student_id = int(input("Enter Student Number: "))
            course_name = input("Enter Course name: ")
            course_index = find_course(course_name, courses_list)
            Student_index = find_student(student_id, student_list)
            if Student_index == -1:
                   print("Student Not Exist")
            else:
                   if course_index == -1:
                       print("Course Not Exist")
                   else:
                       student_list[Student_index].add_course(courses_list[course_index])
                       for i in student_list[Student_index].courses_list:
                           print(i.course_name)
        except:
            print("Error")

    elif x == 0:
        exit()