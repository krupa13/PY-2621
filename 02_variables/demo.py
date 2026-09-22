# Variables
# Assign Data (Store Data)

student_name = "Ravi" # String
student_age = 25 # int
student_gpa = 9.5 # float
student_passed = True # True is a keyword to represent boolean  value True/false i.e Correct/Incorrect
student_failed = False # boolean
# STUDENT_AADHAR = # SyntaxError: invalid syntax
STUDENT_AADHAR = None # Absence of value # NoneType
student_ids = [101,102,103,104,105]

# Retrieve Date (Get Data)
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(student_failed)
print(STUDENT_AADHAR)

# Concatenation: Joining Strings Using + Operator
print("========== Student Info ===========")
print("Student Name: " + student_name)
# print("Student Age: " + student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age: ", student_age)
print("Student GPA: ", student_gpa)
print("Did Student passed: ", student_passed)
print("Did Student failed: ", student_failed)
print("Student Aadhar ID: ", STUDENT_AADHAR)

# type(): Used to tell data type
type(student_name)
print(type(student_name)) # student_name is an object of string class 
print(type(student_age))
print(type(student_age)) # student_age is an object of int class 
print(type(student_passed))
print(type(student_failed))
print(type(STUDENT_AADHAR))
print(type(student_ids))

print("=============================")

# id() used to tell memory address
print(id(student_name))
print(id(student_age)) 
print(id(student_passed))
print(id(student_failed))
print(id(STUDENT_AADHAR))
print(id(student_ids))

print("=======================")