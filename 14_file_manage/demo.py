# File management with python

# Syntax - 1

# file = open("file.txt", "r")

file_data = open("14_file_manage/file.txt", "r")
print(file_data)
print(file_data.read())
print(file_data.closed) # False --> Still Open
file_data.close()
print(file_data.closed) # True --> Now File Is Closed

print("=" * 50)

# syntax 2 - (Recommended)
with open("14_file_manage/file.txt", "r") as file_data:
    print(file_data.read())
print(file_data.closed) # True --> Now File Is Closed

print("=" * 50)

# Create a new file
with open("14_file_manage/write.txt", "w") as file_data:
    print("file created")

print("=" * 50)

# Write Data inside the file
with open("14_file_manage/write.txt", "w") as file_data:
    file_data.write("File created using python")

print("=" * 50)

# Read data from the file
with open("14_file_manage/write.txt", "r") as file_data:
    print(file_data.read())

print("=" * 50)

# Delete the write.txt file
print("Delete File")
import os
os.remove("14_file_manage/write.txt") # NameError: name 'os' is not defined. Did you forget to import 'os'?