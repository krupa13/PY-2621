# Indentation

# -> When to use Space -> When We Write Block Of Code
# -> When Not to use Space -> Single Statement 
# -> How many spaces to use -> At least one space, Python Recommended is 4 Spaces (tab)

print("Good Morning") # when not to use space - Single statement

# print("Good Morning") # IndentationError: unexpected indent
#    print("Good Morning") # IndentationError: unexpected indent

# WHen to use space - when we write a block of code
# class student: # IndentationError: expected an indented block after class definition on line 13
# student_name = "krupa"

# Atleast one space
class student:
 student_name = "krupa"

# Atleast two spaces
class student:
  student_name = "krupa"

# Ten Spaces
class student:
          student_name = "krupa"

# Python recommended 4 spaces (tab)
class student:
    student_name = "krupa"

# Consistent number of spaces
# class student:
#    student_name = "krupa" # 4 spaces
# student_email = "abc@gmail.com" # 1 space # IndentationError: unindent does not match any outer indentation level

class student:
    student_name = "krupa"
    student_email = "abc@gmail.com"
