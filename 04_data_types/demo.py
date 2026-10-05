# Data Types
# Numeric Types

data = 10
print(type(data))

data = -10
print(type(data))

data = 10.5
print(type(data))

# data = a + ib
# data = 5 + i3
# data = a + bj # Python Format
data = 5 +3j
print(type(data))

data = True
print(type(data))

data = False
print(type(data))

data = None
print(type(data))

data = "python"
print(type(data))

# Lists
data = [10,20,30,40,50]
print(type(data))

# Touples
data = (10,20,30,40,50)
print(type(data))

# Sets
data = {10,20,30}
print(type(data))

# Dictionaries
data = {"course": "python","time": 9,"duration": 5}
print(type(data))

# Custom Data Types to Hold Student Data
class Student:
    student_id = 101
    student_name = "Krupa"
    student_mail = "123@gmail.com"
    student_contact = 123456789
    student_gpa = 7.1
    student_enrolled_courses = ["python","ai","cloud"]
    student_courses_prices = (20000,25000)

data = Student()
print(type(data))

# Type Conversion / implicit conversion (Automatic)
n1 = 10 # int
n2 = 5.5 # float
sum = n1 + n2
print(sum)
print(type(sum))

# Type Casting / Explicit Conversion (Manually Done by a developer)
price = 119.99 # float
print(price)
print(type(price))

# Round off Price
round_off_price = int(price)
print(round_off_price)
print(type(round_off_price))

# How Casting Is Needed In Real World Applications 
# Some USer In A Web Site Is Filling Some Form (Text Boxes) -> Behind The Scenes They Are Strings
rating = "2"
print(type(rating))

# if rating >= 4: # TypeError: '>=' not supported between instances of 'str' and 'int'
rating = int(rating)
print(type(rating))
if rating >= 4:
    print("Postive Feedback")
else:
    print("Negative Feedback")