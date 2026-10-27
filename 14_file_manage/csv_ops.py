# Working with CSV files

# Read Data fromt the csv file
with open("14_file_manage/students.csv", "r") as file_data:
    print(file_data.read())

print("=" * 50)

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad
import csv
with open("14_file_manage/students.csv", "r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        # print(row[-1])
        if row[-1] == "Hyderabad":
            print(row)

print("=" * 50)

# Writing Data To CSV File
with open("14_file_manage/emp.csv", "w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(["name","email","mobile","address"])
    csv_writer.writerow(['John',"john@gmail.com","123456789","Bangalore"])