# Conditional Statements (Decision Making Statements)

# if
if True:
    print("This")
    print("is")
    print("block")
    print("of")
    print("code")

print("===========================")

if False: # Code is not analyzed because condition is statically evaluated as false 
    print("This")
    print("is")
    print("block")
    print("of")
    print("code")

# If condition with dynamic
if 5 > 2:
    print("Yes 5 > 2 is correct")

if 5 < 2:
    print("Yes 5 < 2 is correct")

num = 10
if num > 0:
    print("Given num is positive")
if num < 10:
    print("Given num is negative")

num = -10
if num > 0:
    print("Given num is poistive")
if num < 10:
    print("Given num is negative")

print("===================")

# if else
num = -10
if num > 0:
    print("Num is positive")
else: # if condition is false
    print("Num is negative")

print("===================")

# Without input() data is hardcoded / fixed
name = "Krupa" # this is fixed i.e static
print(name)

# With input() data is dynamic
# name = input("Enter your name:")
# print(name)

print("===================")

# username = input("enter your username:")
# print(username)
# print("Welcome: "+username) # + Operator Concatenation 
# print("Welcome: ",username) # , Operator 
# print("Welcome: {username}") # , No Interpolation
# print(f"Welcome: {username}") # Interpolation

print("===================")

# num = input("Enter your number:")
# num = int(num)
# if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
#     print(f"Given num {num} is positive")
# else:
#     print(f"given num {num} is negative")

print("=======================")

# Voting Application Dynamic 
# age = input("Enter Your Age: ")
# age = int(age)
# age = int(input("Enter your Age: "))
# if age >= 18:
#     print("You can VOte")
# else:
#     print("You cannot vote")

# Conditional Expression
# age = int(input("Enter your Age: "))
# # Value_if_true if condition else value_if_false
# print("You can vote" if age >=18 else "You cannot vote")

print("=======================")

# Say if i want to check if a student is passed or failed
# marks = int(input("Enter your marks: "))
# if marks >= 35:
#     print("You are passed")
# else:
#     print("You are failed")

print("=======================")

# Say I Want To Check For Grades
# elif ladder
# 90 and above - A Grade
# 75 and above but below 90 - B Grade
# 60 and above but below 75 - C Grade
# 50 and above but below 60 - D Grade
# 35 and above but below 50 - E Grade
# Below 35 Failed

# marks = int(input("Enter your marks: "))
# if 90 <= marks <= 100:
#     print("A Grade")
# elif 75 <= marks < 90:
#     print("B Grade")
# elif 60 <= marks < 75:
#     print("C Grade")
# elif 50 <= marks < 60:
#     print("D Grade")
# elif 35 <= marks < 50:
#     print("E Grade")
# else:
#     print("Invalid Marks! Out of 0 to 100 Marks")

print("=======================")

# Match Case
# error_code = int(input("Enter the HTTP status code you are seeing: "))
# match error_code:
#     case 200:
#         print("Success - OK")
#     case 300:
#         print("Moved Permanently")
#     case 400:
#         print("bad request")
#     case 404:
#         print("Error Page Not Found")
#     case 500:
#         print("Error Server Not Responding")
#     case 502:
#         print("Bad Gateway")
#     case 503:
#         print("Service Unavailable")
#     case _:
#         print("Unkown Error Code")

print("===================") 

# Match Case
user_role = input("Enter your User Role: ")
match user_role:
    case "admin":
        print("Full Access")
    case "student":
        print("Read only access")
    case "trainer":
        print("Read and write access")
    case _:
        print("Unauthorized User Role")