# Operators

# Arithmetic Operators

num1 = 10
num2 = 5

print("sum of numbers: ", num1 + num2)
print("Substact Numbers: ", num1 - num2)
print("Multiplication of Numbers: ", num1 * num2)
print("Division of Numbers: ", num1 / num2)
print("modula of numbers: ", num1 % num2)

print("Normal Division: ", 3/2) # 1.5

print("Floor Division: ", 3//2) #  1

print("exponentiation: ", 3 ** 2) # 3 to the power of 2

print("============================")

# Compound Assignement Operators

num = 10
num = num + 5 # Long Form
print(num)

num = 10
num +=5 # Short Form
print(num)

# Increment and Decrement operators

count = 1000
print(count)
# count++ # SyntaxError: invalid syntax
count += 1
print(count)

count -= 1
print(count)

print("============================")

# Comparision Operator
num1 = 3
num2 = 5
print(num1 > num2)
print(num1 < num2)
print(num1 != num2)

print("============================")

# Logical Operators
num1 = 4
num2 = 5
num3 = 2
num4 = 3
print(num2 > num3 and num4 > num1)
print(num1 > num3 or num2 < num4)
print(not num3 > num1)

print("============================")

# Membership operators

data = "Python is a programming language"
find_word = "java"
status = find_word in data
print(status)

emp_ids = [100,101,102,103,104,105,109]
id = 108
status = id in emp_ids
print(status)

print("============================")

# Identity Operators

value_x = 10
value_y = 100
value_z = 10

print(value_x is value_y)
print(value_x is value_z)
print(value_y is value_z)

print("============================")

# Bitwise Operators
n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
   # | # 0000000000000111
   # & # 0000000000000001
print(n1 | n2) # 7
print(n1 & n2) # 1