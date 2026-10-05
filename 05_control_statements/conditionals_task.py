# Task 1: Positive Number Checker
# Ask the user to enter a number. If the number is positive, print: Positive Number

positive_num_checker = float(input("Enter a Number: "))
if positive_num_checker > 0:
    print("Positive Number")

print("=====================================")

# Task 2: Voting Eligibility
# Ask for age. If age is 18 or above, print: Eligible to Vote
age = int(input("Enter your Age: "))
if age >= 18:
    print("Eligible to VOte")

print("=====================================")

# Task 3: Discount Coupon
# Ask for purchase amount. If amount is greater than 5000, print: Coupon Applied
amount = int(input("Enter the amount: "))
if amount > 5000:
    print("Coupen Applied")

print("=====================================")

# Task 4: Free Delivery
# Ask for order value. If order value is greater than 1000, print: Free Delivery Available
order_value = int(input("Enter order value: "))
if order_value > 1000:
    print("Free delivery available")

print("=====================================")

# Task 5: Login Notification
# Ask for username. If username is "admin", print: Welcome Admin
username = input("Enter user name: ")
if username == "admin":
    print("Welcome Admin")

print("=====================================")

## IF-ELSE TASKS
# Task 1: Even or Odd
# Ask for a number. If even → print "Even" Else → print "Odd"
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("=====================================")

# Task 2: ATM PIN Validation
# Store: actual_pin = 1234
# Ask user for PIN. Correct → Transaction Success Wrong → Transaction Failed
actual_pin = 1234
pin = int(input("Enter the PIN: "))
if pin == actual_pin:
    print("Transaction Success.")
else:
    print("Transaction Failed.")

print("=====================================")

# Task 3: Pass or Fail
# Ask marks. Marks >= 35 → Pass Else → Fail
marks = int(input("ENter your marks: "))
if marks >= 35:
    print("Passed")
else:
    print("Failed")

print("=====================================")

# Task 4: Login Validation
#Store: password = "python123"
# Ask user password. Correct → Login Successful Else → Incorrect Password
password = "python123"
login = input("Enter the password: ")
if login == password:
    print("Login Succesfull")
else:
    print("Incorrect password")

print("=====================================")

# Task 5: Balance Check
# Ask withdrawal amount. Balance: balance = 5000
# Amount <= balance → Withdrawal Success Else → Insufficient Balance
balance = 5000
amount = int(input("Enter withdraw amount: "))
if amount <= balance:
    print("Withdraw Success")
else:
    print("Insufficient Balance")

print("=====================================")

# ELIF TASKS
# Task 1: Income Tax Slab
# Income > 10 Lakhs → 30%, Income > 5 Lakhs → 20%, Income > 2 Lakhs → 10% Else → No Tax
income = float(input("Enter your annual income: "))
if income > 1000000:
    print("Income Tax 30%")
elif 500000 <= income < 1000000:
    print("Income Tax 20%")
elif 200000 <= income < 500000:
    print("Income Tax 10%")
else:
    print("No Income Tax")

print("=====================================")

# Task 2: Movie Ticket Pricing
# Age < 5 → Free Age < 18 → ₹100 Age < 60 → ₹200 Else → ₹150
age = int(input("Enter your age: "))
if age <= 5:
    print("Movie Ticket Free")
elif 18 >= age > 5:
    print("Movie Ticket price is 100 rupees")
elif 60 >= age > 18:
    print("Movie Ticket price is 200 rupees")
else:
    print("Movie Ticket price is 150 rupees")

print("=====================================")

# MATCH-CASE Tasks
# Task 1: ATM Menu, 1 -> Deposit, 2 -> Withdraw, 3 -> Balance, 4 -> Exit
atm_menu = int(input("Enter the options from 1-4: "))
match atm_menu:
    case 1:
        print("Deposit")
    case 2:
        print("Withdraw")
    case 3:
        print("Balance")
    case _:
        print("Exit")

print("=====================================")

# Task 4: Student Course Selection
# Task 2: 1 → Python 2 → Java 3 → DevOps 4 → Data Science
course = int(input("Enter the selected option 1-3: "))
match course:
    case 1:
        print("Python")
    case 2:
        print("Java")
    case 3:
        print("Data Science")
    case _:
        print("Devops")

print("=====================================")

# 🚀 Challenge Task (Combines Everything)
# Student Login Portal
# Ask username and password
# Validate using if-else
# After successful login show menu using match-case
# 1. View Profile
# 2. Change Password
# 3. Logout
# Use elif for role-based access:
# Marks >= 90 → Gold Student
# Marks >= 75 → Silver Student
# Marks >= 50 → Bronze Student
# if
# if-else
# elif
# match-case
# input handling
# real-world logic
# Perfect as a mini assignment after completing conditionals.

actual_username = "Krupa"
actual_password = "Krupa123"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == actual_username and password == actual_password:
    print("successful login")
    menu = int(input("Enter the menu options between 1-3: "))
    match menu:
        case 1:
            print("View Profile")
        case 2:
            print("Change Password")
        case 3:
            print("Logout")
    marks = int(input("Enter your marks: "))
    if 90 <= marks <= 100:
        print("Gold Student")
    elif 75 <= marks < 90:
        print("Silver Student")
    elif 50 <= marks < 75:
        print("Bronze Student")
    else:
        print("Marks should be between 0-100")
else:
    print("Invalid credentials")