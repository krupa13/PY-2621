# String Methods

greet = "hi"
print(greet)
# print(dir(greet))

print("=" * 20)

# String methods are for manipulation, transformation and validation

# Below is the example of the Manipulation

# capitalize(): returns a capitalized version of the string
# More spefically, it makes the first character of the string upper case, rest lower case
greet = "hi"
result = greet.capitalize()
print(result)

# Simulate gmail functionality - Transformation
# KruPAraOMUi --> kruparaomui@gmail.com

# email = input("Enter the email ID: ")
# print("Original Email ID: " + email)

# lower(): Converts string to lowercase
# transformed_email = email.lower()
# print("Transformed Email: " + transformed_email)

# Add domain to the email address
# domain = "@gmail.com"
# transformed_email = transformed_email + domain
# print("Final email address: " + transformed_email)

print("=" * 20)

# Simulate PAN CARD functionality - validation

# PAN = input("Enter valid PAN ID: ")
# print("Original PAN ID: " + PAN) # @anomp9912w(wrong)-> anomp9912w(to upper) -> an12(wrong)

# # isalnum(): returns True if all characters in the string are alphanumeric(letters or num)
# valid_PAN = PAN.isalnum()
# print(f"Given {PAN} is {valid_PAN}")

# valid_PAN = PAN.isalnum() and len(PAN) == 10
# print(f"Given {PAN} is {valid_PAN}")

# if PAN.isalnum() and len(PAN) == 10:
#     print("Original PAN ID: " + PAN)
#     # upper(): converts the string to upper case
#     print("Transformed PAN: " + PAN.upper())
# else:
#     print(f"Given {PAN} is INVALID")

# A valid PAN is a 10-character alphanumeric code. 
# The first five characters are letters, the next four are numbers, 
# and the last character is a letter (e.g., ABCDE1234F)

print("=" * 50)

# PAN = input("Enter PAN ID: ")
# print("Original PAN given: " + PAN)

# if len(PAN) == 10:
#     first_five = PAN[0:5:1] # First five
#     middle_four = PAN[5:9:1] # Next four
#     last_one = PAN[-1] # Last one

#     # isalpha(): check if a string is pure alphabet or not
#     # isdigit(): check is a string is pure digit or not
#     if first_five.isalpha() and middle_four.isdigit() and last_one.isalpha():
#         print("Transformed PAN: " + PAN.upper())
#     else:
#         print(f"Given {PAN} is INVALID.")
# else:
#     print("Given PAN should be 10 characters only.")

print("=" * 50)

# VERIFY GST NUMBER functionality - validation
# A valid GST number is a 15 character alphanumeric code --> Ex: 37ABCDE1234F1Z5
# First two characters are numbers
# Next five characters are letters
# Next four are numbers
# Next one is letter
# Next one is number
# Next one is letter
# next one is number

GST = input("Enter the GST number: ")
print("Original entered GST number: " + GST)

# Check the characters are alphanumeric and length
if len(GST) == 15:
    state_code = GST[0:2:1] # check first two are digits
    next_five = GST[2:7:1] # check next five are letters
    next_four = GST[7:11:1] # check next 4 are numbers
    next_one = GST[11] # next one is letter
    entity_code = GST[12]
    default_alphabet = GST[13]
    checksum_digit = GST[14]

    # isalpha(): check the given string is pure alphabet or not
    # isdigit(): check the given string is pure digit or not
    if state_code.isdigit() and next_five.isalpha() and next_four.isdigit() and next_one.isalpha() and entity_code.isdigit() and default_alphabet.isalpha() and checksum_digit.isdigit():
        print("Transformed GST Number: " + GST.upper())
    else:
        print(f"Given {GST} is INVALID.")
else:
    print("Given GST should be 15 characters only.")


# check entered PAN is real or not --> we have to work connecting with DB in this case
# Below code is sample of DB connection how real PAN verification works.

# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="your_user",
#     password="your_password",
#     database="your_database",
# )

# pan_id = "ABCDE1234F"

# try:
#     with conn.cursor() as cursor:
#         cursor.execute(
#             "SELECT 1 FROM your_table WHERE PAN_ID = %s LIMIT 1",
#             (pan_id,),
#         )
#         exists = cursor.fetchone() is not None

#     print("Record exists" if exists else "Record does not exist")
# finally:
#     conn.close() 