# Lists

# empty list
empty_list = []
print(type(empty_list))
print(empty_list)

empty_list = list()
print(type(empty_list))
print(empty_list)

# list with numeric data
data = [10,20,30,40]
print(data)

# list with text data
data = ["python", "ai"]
print(data)

# list with mixed data
data = [10,20,30,"python", 8.8, True]
print(data)

# Accessing data in Lists
data = [10,20,30,40]

# First Element
first_element = data[0]
print(first_element)

# Last Element
last_element = data[-1]
print(last_element)

# unknown_element = data[10] --> IndexError: list index out of range
# print(unknown_element)

# Slicing
data = [10,20,30,40,50]
print(data[1:4:1])
print(data[0:5:1])

# Accessing individual Elements --> 10K elements
data = [10,20,30,40,50,60]

# Loops
for num in data:
    print(num)

# Operators -> Requirement: Multiply Each Number with 10 
data = [10,20,30]
for num in data:
    print(num * 10)

# Requirement: Convert Courses To Upper Case
data = ["python", "ai"]
for course in data:
    print(course.upper())

# Conditionals -> Requirement: Get Only Even Numbers
data = [10,20,25,30,40,45,50,55]
for num in data:
    if num % 2 == 0:
        print(num)

# Duplicates Allowed 
data = [10,20,10,30,40,10,50,10]
print(data)

# Insertion Order Preserved 
data = [10,20,30,40,50]
print(data)

# List Operations / Methods 
data = [10,20,30,40,50]
print(dir(data))