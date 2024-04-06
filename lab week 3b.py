#NAMES

#fix the problems with each of these classes (1-3)
#(run them to see the traceback)

#1
class MyClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#2
class MyClass():
    def __init__(self):
        a = 10
        b = 20
        self.x = a + b
my_instance = MyClass()
my_instance.x

#3
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#4 Create a class to hold all of the courses a student at Harris is enrolled in.
#  - The instance should take two arguments when created; student name, 
#    and student year
#  - At startup, each instance should have an empty list as an attribute 
#    named "enrolled_courses"
#  - Create a method named "enroll" that takes some arguments that describe
#    a course, e.g. name, course number, days, times
#  - When called, make the "enroll" method add a course to the "enrolled_courses"
#    list
#  - Finally, think about what other methods you could add. One to drop a course?
#    One to display the enrolled courses?  Or could you modify "enroll" to make
#    sure times don't overlap, or there aren't too many courses in the list?
#    Work on these if you would like an extra challenge.

class MyCourses():
    def __init__(self, student_name, year):
        self.student_name = student_name
        self.year = year
        self.enrolled_courses = []
    def enroll(self, class_name, class_number, days, times):
        course_details = { 
            "name": class_name,
            'number': class_number,
            "days": days,
            "times": times
        }
        self.enrolled_courses.append(course_details)
  

student = MyCourses('Sarah', 2025)
student.enroll = ('Python', 'PPHA-3012-02','TTH','9:00-10:20 AM')
print("Enrolled Courses for:", student.student_name, student.year)
for course in student.enrolled_courses:
    print("Name:", course["class_name"], "Number:", course["class_number"], "Days:", course["days"], "Time:", course["times"])
