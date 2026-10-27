# Exception Handling
# When there is no error, nothing to handle

print("Program execution started")

num1 = 10
num2 = 5

print("Result: ", num1/num2)

print("Program execution completed")

print("=" * 30)

# When errors occurs, program excution stops

print("Program execution started")

num1 = 10
num2 = "5"

# print("result: ", num1/num2 ) # TypeError: unsupported operand type(s) for /: 'int' and 'str'

print("Program execution completed")

print("=" * 30)

# When errors occurs, we have to handle Exceptions

print("Program execution started")

num1 = 10
num2 = "5"

try:
    print("Result", num1/num2)
except:
    print("WARNING!!! Don't Divide Numeric Values With Strings/Text")

print("Program execution completed")

print("=" * 30)

# When Errors Occurs -> We Want To Handle Exceptions

print("Program execution started")

num1 = 10
num2 = 5

try:
    print("Result:", num1/num2)
except:
    print("WARNING!!! Don't Divide Numeric Values With Strings/Text")

print("Program execution completed")

print("=" * 30)

print("Program execution started")

num1 = 10
num2 = 0

# print("Result", num1/num2) # ZeroDivisionError: division by zero

print("Program execution completed")

print("=" * 30)

print("Program execution started")

num1 = 10
num2 = 0

try:
    print("result", num1/num2)
except:
    print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")

print("Program execution completed")

print("=" * 30)

# When we come across multiple errors

print("Program execution started")

# data = [1,2,"three",0,4]
# data = [1,2,0,4]
data = [1,2,3,4]

for num in data:
    print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero

print("Program execution completed")

print("=" * 30)

# when we come across multiple errors

print("Program execution started")

data = [1,2,"three",0,4]

for num in data:
    try:
        print(1/num) # 1/1 - 1/2 - 1/'three' - 1/0 - 1/4
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        # ZeroDivisionError: division by zero
    except:
        print("OOPS!!!! Something Went Wrong")

print("Program execution completed")

print("=" * 30)

# when we come across multiple errors

print("Program execution started")

data = [1,2,"three",0,4]

for num in data:
    try:
        print(1/num)
    except TypeError:
        print("OOPS!!!! Don't Divide Numeric Values With Strings/Text")
    except ZeroDivisionError:
        print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")

print("Program execution completed")

print("=" * 30)

# ELSE -- when there is no error, execute  this code block

print("Program execution started")

num1 = 10
num2 = 0

try:
    print("Result", num1/num2)
except:
    print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation was successfull")

print("Program execution completed")

print("=" * 30)

# ELSE -- when there is no error, execute  this code block
print("Program execution started")

num1 = 10
num2 = 5

try:
    print("Result", num1/num2)
except:
    print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation was successfull")

print("Program execution completed")

print("=" * 30)

# Finally --- Runs the block of code whether an exception is raised or not

print("Program execution started")

num1 = 10
num2 = 5

try:
    print("Result: ", num1/num2) # Verify Login Credentials
except:
    print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation was successfull") # Then Only Check For OTP
finally:
    print("Close all opened data streams and DB connections")

print("Program execution completed")

print("=" * 30)

# Finally ---  runs the block of code whether an excpetion raised or not
 
print("Program execution started")

num1 = 10
num2 = 0

try:
    print("result: ", num1/num2)
except:
    print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation was successfull")
finally:
    print("Close all opened data streams and DB connections")

print("Program execution completed")

print("=" * 30)

# without user defined exceptions and raise keyword
print("Program execution started")

age = int(input("Enter your Age: "))

if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")

print("Program execution completed")

print("=" * 30)

# with user defined exceptions and raise keyword
print("Program execution started")

class UnderAgeError(Exception):
    pass

age = int(input("Enter your age: "))

if age < 18:
    # raise typeerror # unrelated error
    # raise underageerror
    raise UnderAgeError("Below 18 Are Not Allowed To Vote")
else:
    print("You can vote")

print("Program execution completed")