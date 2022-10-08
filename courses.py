class Course:
    def __init__(self,course_id,course_name,course_class):
        self.course_id = course_id
        self.course_class = course_class
        self.course_name = course_name

    def get_course_details(self):
        print(str(self.course_id) + "\t\t" + self.course_name + "\t\t"+self.course_class)
