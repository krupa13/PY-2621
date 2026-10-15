# Student Management System

# Menu Based System -> In Future When You Learn Frontend(HTML/CSS/JS), 
# Replace Menus With UI Elements Like Buttons 

# SYSTEM Info --> READ only (Tuple)
SYSTEM_INFO = ("Digital Tech", "Student Management System", "V1")

# ADMIN INFO --> READ ONLY (Tuple)
ADMIN_INFO = ("9999999999", "admin@digital.com")

# Display System Info 
print("=" * 50)

print(f"            Welcome to {SYSTEM_INFO[0]}")
print(f"    Software Name is {SYSTEM_INFO[1]} --- {SYSTEM_INFO[-1]}")

print("=" * 50)

# Implement Core Functionalities (CRUD)
# Add Student -> ID, Name, Scores & SKills 
# Student Data Representation
        # students = {
        #     "101":{
        #         "name": "Ravi",
        #         "scores": [90,80,80,70],
        #         "skills": {"python","ai"}
        #     },
        #     "102":{
        #         "name": "John",
        #         "scores": [90,80],
        #         "skills": {"java","sql"}
        #     }
        # }

# Students dictionary is where we will store the data
students = {}

# Build the menu for CRUD operations
while True:
    print("=" * 30)
    print("     Choose an Option: ")
    print("=" * 30)

    print("1 - Create Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit Application")

    choice = input("Enter your choice between 1-5: ")

    if choice == "1":
        # Create Student
        print("=" * 30)
        print("     Creating Student")
        print("=" * 30)

        student_id = input("Enter Student ID: ") # 101

        if student_id in students:
            print("=" * 50)
            print(f"OOPS! Student ID {student_id} already exists.")
            print("=" * 50)

        else:
            name = input("Enter Name: ").title() # krupa rao

            scores = []

            while True:
                score_input = input("Enter Score or type Done: ") # 90, 80, done
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print(f"Invalid score {score_input}, Score should be (0-100) only.")
                else:
                    print(f"Invalid Score {score_input}, Score should be digit only.")

            skills = set()

            while True:
                skill_input = input("Enter Skill or type done: ") # Python, ai, done, or ai
                if skill_input == "done":
                    break
                else:
                    skills.add(skill_input)

            print(students) # before adding

            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }

            print(students) # After adding

    elif choice == "2":
        # Update Student 
        print("=" * 30)
        print("     Updating Student")
        print("=" * 30)

        student_id = input("Enter ID to update: ") # 101

        if student_id in students:
            new_name = input("Enter New Name: ").title() # krupa rao
            students[student_id]['name'] = new_name

            print("=" * 50)
            print(f"Student ID {student_id} is updated successfully.")
            print("=" * 50)

        else:
            print("=" * 50)
            print(f"OOPS! Student ID {student_id} does not exist.")
            print("=" * 50)

        print(students) # After updating

    elif choice == "3":
        # Delete Student
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)

        student_id = input("Enter student ID: ") # 101

        if student_id in students:
            students.pop(student_id)
            print("=" * 50)
            print(f"Student ID {student_id} deleted successfully.")
            print("=" * 50)
        else:
            print("=" * 50)
            print(f"OOPS! Student ID {student_id} does not exist.")
            print("=" * 50)

        print(students) # After Deleting

    elif choice == "4":
        # Read Student 
        print("=" * 30)
        print("     Reading Student")
        print("=" * 30)

        student_id = input("Enter Student ID: ") # 101

        if student_id in students:
            # Fetch Specific Student Data
            # {'101': {'name': 'Ravi', 'scores': [90], 'skills': {'python'}}}
            data = students[student_id]

            # data = {'name': 'Ravi', 'scores': [90,80], 'skills': {'python','ai'}}
            name = data['name']
            scores = data['scores']
            skills = data['skills']

            # Average Score
            total_score = 0 # 90 + 80 + 90
            current_score_count = 0 # 0 + 1 + 2

            for score in scores:
                total_score += score
                current_score_count += 1

            average_score = total_score / current_score_count

            # Highest Score [90,80,100]
            high_score = scores[0]

            for score in scores:
                score > high_score
                high_score = score

            # Lowest Score
            low_score = scores[0]

            for score in scores:
                score < low_score
                low_score = score

            # SKill count
            skill_count = 0

            for skill in skills:
                skill_count += 1

            print("=" * 50)
            print(f"    Reading Student {student_id} details.")
            print("=" * 50)

            print(f"Student ID: {student_id}")
            print(f"Student Name: {name}")
            print(f"All scores: {scores}")
            print(f"Average Score: {average_score}")
            print(f"Highest Score: {high_score}")
            print(f"Lowest Score: {low_score}")
            print(f"All SKills: {skills}")
            print(f"Skills Count: {skill_count}")

        else:
            print("=" * 50)
            print(f"OOPS! Student ID {student_id} does not exist.")
            print("=" * 50)

    elif choice == "5":
        # Exit Application
        print("=" * 30)
        print("     Exiting Application")
        print("=" * 30)

        # Display admin info
        print("=" * 50)
        print(f"    Admin contact number {ADMIN_INFO[0]}")
        print(f"    Admin email address {ADMIN_INFO[1]}")
        print("=" * 50)
        break

    else:
        # Invalid Choice
        print("=" * 30)
        print("     Invalid option, choose between 1-5")
        print("=" * 30)

