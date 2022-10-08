import random

class Student:
    def __init__(self,student_number,student_name,student_class):
        # self.student_number = random.randint(1, 200)
        self.student_number = student_number
        self.student_name = student_name
        self.student_class = student_class
        self.courses_list = []



    def add_course(self, courses):
        if self.student_class == courses.course_class:
            for i in self.courses_list:
                if courses.course_id == i.course_id:
                    print("Course Already exists")
                    return
            self.courses_list.append(courses)
            print("Course add successfully to Course List")
        else:
            print("Invalid Course Class")


    def getStudents(self):
        print(f" Student ID: {self.student_number} Student Name: {self.student_name} Student Class: {self.student_class}")
        if len(self.courses_list) == 0:
            print("There is no courses")
            return
        print("Courses List: ")
        for course in self.courses_list:
            course.get_course_details()
            # print(course.course_name)