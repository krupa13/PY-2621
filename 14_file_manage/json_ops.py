# Working with JSON files/Data

import json

student = {
    'id': 101,
    'name': 'Krupa',
    'courses': ['python', 'ai'],
    'gpa': 7.2
}

print(type(student))
print(student)

print("=" * 50)

# Create JSON file and write data
with open("14_file_manage/student.json", "w") as file_data:
    json.dump(student, file_data)

print("=" * 50)

# Create JSON File and Write Data With Indentation
with open("14_file_manage/student.json", "w") as file_data:
    json.dump(student, file_data, indent=4)

print("=" * 50)

# Read that JSON file
with open("14_file_manage/student.json", "r") as file_data:
    data = json.load(file_data)
    print(data)

print("=" * 50)

# From Given JSON File, Read Student Name and Courses He Enrolled
with open("14_file_manage/student.json", "r") as file_data:
    data = json.load(file_data)
print("Student Name: ", data['name'])
print("Courses Name: ", data['courses'])
