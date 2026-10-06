# strings

# single line strings
s1 = 'hello' # recommended
print(s1)
print(type(s1))

s1 = "hello"
print(s1)
print(type(s1))


s1 = '''hello world''' # not recommended
print(s1)
print(type(s1))

s1 = """hello string""" # not recommended
print(s1)
print(type(s1))

# Multi Line Strings

# define_python = 'Python is a high-level, general-purpose programming language 
#         that emphasizes code readability, simplicity, and ease-of-writing 
#         with the use of significant indentation, an extensive ("batteries-included") 
#         standard library, and garbage collection.'

define_python = '''Python is a high-level, general-purpose programming language 
        that emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, an extensive ("batteries-included") 
        standard library, and garbage collection.'''

print(define_python)
print(type(define_python))

define_python = """Python is a high-level, general-purpose programming language 
        that emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, an extensive ("batteries-included") 
        standard library, and garbage collection."""

print(define_python)
print(type(define_python))

# When you use single quote in a string, enclose them in double quotes
question = "how are you?"
# answer = 'i'm fine' -- Wrong
answer = "I'm fine"
print(answer)

# When you use double quote in a string, enclose them in single quotes
question = "how are you?"
# answer = "I"m fine"" -- wrong
answer = 'I"m fine'
print(answer)

# Accessing Strings 
text = "python"
print(text[0])
print(text[1])

print(text[-1])
print(text[-2])

# print(text[10]) # IndexError: string index out of range

# slicing

text = "python"
# len(): Gives Length Of Object
print(text[:])
print(text[0:4:1])
print(text[1:3])
print(text[0:5:2])

                # 0   1 2  3  4  5
                # p   y t  h  o  n
                # -6 -5 -4 -3 -2 -1  

print(text[-4:-2:1])
print(text[-4:-1:2])
print(text[-4:-1:-1])
print(text[-4:-6:-1])

# String Concatenation 
s1 = "Good "
s2 = "Morning"
print(s1+s2)

# Formatted String Literals (f-strings)
age = 30
print(f"My age is {age}")

# String Repetition
laugh = "haha"
print(laugh)

hard_laugh = laugh * 5
print(hard_laugh)

# string immutability
greet = "hi"
print(greet)

print(greet[0])
# greet[0] = "HI" # TypeError: 'str' object does not support item assignment
# print(greet[0])

# Example For Mutable Data Type i.e List 

greet = ['h', 'i']
print(greet[0])
greet[0] = "H"
print(greet[0])