# OOP -- Object Oriented Programming

# Class -- Blue print

class Student:

    # Object "HAS" something like characteristics / Properties (Variables)
    # Student HAS - name, email, gender
    student_name = "krupa"
    student_email = "krupa@gmail.com"

    # Object DOES something like behaviors / actions (methods)
    # Student DOES - Studies, Actions, Exams etc.,
    def student_studies():
        print("Student is studying python")

# This is a normal function, as it is outside the class
# def student_studies():
#     print("Studying python")

# To use this class, we need an Object
student_object = Student()

# print("Student Name: ", student_name) # NameError: name 'student_name' is not defined
# print("Student Email: ", student_email) # NameError: name 'student_email' is not defined

print("student name: ", student_object.student_name)
print("student email: ", student_object.student_email)
# student_object.student_studies() # TypeError: Student.student_studies() takes 0 positional arguments but 1 was given

print("=" * 50)

# Class - Blue Print

class Student:

    # Object "HAS" something like characteristics / Properties (Variables)
    # Student HAS - name, email, age
    student_name = "krupa"
    student_email = "krupa@gmail.com"

    # Object DOES something like behaviors / actions (Methods)
    # Student DOES -- studies, exams, attendance etc.,
    def student_studies(self):
        print("student studying python")

# To use this class, we need an object
student_object = Student()

print("Student Name: ", student_object.student_name)
print("student email: ", student_object.student_email)

student_object.student_studies()

print("=" * 50)

# Working With Multiple Objects 
# class - Blue Print

class Student:

    # Object HAS something like characteristics / behaviors (Variables)
    # Student HAS  - name, email, age
    student_name = "krupa"
    student_email = "krupa@gmail.com"

    # Object DOES something like behaviors / Actions (Methods)
    # Student DOES - exams, attendace, studies etc.,
    # Self is object reference
    def student_studies(self):
        print("Student studying python")
        print("Student Name: ", self.student_name) # Recommended
        print("Student Email: ", self.student_email) # Recommended

# To use this class, we need an object
student_krupa = Student()
student_krupa.student_studies()

print("=" * 50)

student_john = Student()
student_john.student_studies()

print("=" * 50)

# Working With Multiple Objects 
# Class - Blue Print 

class Student:

    # Object HAS something like characteristics / behaviors (Variables)
    # Student HAS  - name, email, age
    # student_name = "krupa"
    # student_email = "krupa@gmail.com"

    # constructor
    def __init__(self, student_name, student_email):
        print("Constructor Call")
        self.student_name = student_name
        self.student_email = student_email

    # Object DOES something like behaviors / Actions (Methods)
    # Student DOES - exams, attendace, studies etc.,
    # Self is object reference
    def student_studies(self):
        print("Student is studying python")
        print("student name: ", self.student_name)
        print("student email: ", self.student_email)

# # To use this class, we need an object
student_krupa = Student("Krupa", "krupa@gmail.com")
student_krupa.student_studies()

print("=" * 50)

student_john = Student("John", "John@gmail.com")
student_john.student_studies()

print("=" * 50)

# Working With Multiple Objects 
# Class - Blue Print 
class Student:

    # Class Variables - Shared Data
    institute_name = "Digital Marketing"
    course = "python"

    # Constructor
    def __init__(self,student_name,student_email):
        print("Constructor Call")
        # Object "HAS" Something like Characteristics / Properties (Variables)
        # Student Has - Name, Email, Gender, Course etc 
        # Instance Variables - self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email

    # Object "DOES" Something like Behaviors / Actions (Methods)
    # Student Does - Studies, Attends, Takes Exams etc 
    # self is object reference
    # Instance Method 
    def student_studies(self):
        print(f"Welcome to {self.institute_name}") # not recommended
        print("Student is studying: ", Student.course) # Recommended
        print("Student name: ", self.student_name)
        print("student email: ", self.student_email)

    # Class Method
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name

    # Static Method
    @staticmethod
    def calculator(num1,num2):
        print(f"Sum Is: ", num1 + num2)
        print(f"Product Is: ", num1 * num2)

# To use this class, we need an object
student_krupa = Student("Krupa", "krupa@gmail.com")
student_krupa.student_studies()

print("=" * 50)

student_john = Student("John", "John@gmail.com")
student_john.student_studies()

print("=" * 50)

# Calling class method
Student.change_institute_name("Digital New merketing")

student_krupa = Student("Krupa", "krupa@gmail.com")
student_krupa.student_studies()

print("=" * 50)

student_john = Student("John", "John@gmail.com")
student_john.student_studies()

print("=" * 50)

# Calling Static Method
Student.calculator(10,5)

# Working with multiple objects
# Class - Blue print
class Student:

    # Class Variables - Shared Data
    institute_name = "Digital Marketing"
    course = "python"

    # Constructor
    def __init__(self, student_name, student_email):
        print("Constructor Call")
        # Object "HAS" something like characteristics/properties (Actions)
        # Student Has - Name, Email, Gender, Course etc 
        # Instance Variables - self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email

    # Object "DOES" Something like Behaviors / Actions (Methods)
    # Student Does - Studies, Attends, Takes Exams etc 
    # self is object reference
    # Instance Method
    def student_studies(self):
        print(f"Welcome to {self.institute_name}") # not recommended
        print("Student Course: ", Student.course) # recommended
        print("Student name: ", self.student_name)
        print("Student Email: ", self.student_email)

    # Class Method
    @classmethod
    def change_insitute_name(cls,new_name):
        cls.institute_name = new_name

    # Static Method
    @staticmethod
    def calculator(num1,num2):
        print(f"Sum IS: ", num1+num2)
        print(f"Substract IS: ", num1-num2)
        print(f"Product IS: ", num1*num2)

# To use this class, we need an object
student_krupa = Student("Krupa", "krupa@gmail.com")
student_krupa.student_studies()

print("=" * 50)

student_john = Student("John","john@gmail.com")
student_john.student_studies() 

print("=" * 50)

# Calling class methods
Student.change_insitute_name("Digital New Marketing")

student_krupa = Student("Krupa", "krupa@gmail.com")
student_krupa.student_studies()

print("=" * 50)

student_john = Student("John","john@gmail.com")
student_john.student_studies() 

print("=" * 50)

# Calling Static Method
Student.calculator(20,5)

print("=" * 50)