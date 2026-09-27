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
name = input("Enter your name:")
print(name)

print("===================")

username = input("enter your username:")
print(username)
print("Welcome: "+username) # + Operator Concatenation 
print("Welcome: ",username) # , Operator 
print("Welcome: {username}") # , No Interpolation
print(f"Welcome: {username}") # Interpolation

print("===================")

num = input("Enter your number:")
num = int(num)
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print(f"Given num {num} is positive")
else:
    print(f"given num {num} is negative")

print("=======================")

# Voting Application Dynamic 
# age = input("Enter Your Age: ")
# age = int(age)
age = int(input("Enter your Age: "))
if age >= 18:
    print("You can VOte")
else:
    print("You cannot vote")