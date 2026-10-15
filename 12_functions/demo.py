# # Functions

# # without Functions
# num1 = 10
# num2 = 5

# # Mathmetical Operations
# print(num1 + num2)
# print(num1 * num2)
# print(num1 - num2)

# print("=" * 50)

# # with functions
# def math_ops():
#     print(num1 + num2)
#     print(num1 * num2)

# # User One Wants To Calculate Mathematical Operations For Below Values
# num1 = 10
# num2 = 5
# print(math_ops())

# print("=" * 50)

# # With Parameters 
# # math_ops(1,2) # TypeError: math_ops() takes 0 positional arguments but 2 were given
# def math_ops(num1, num2):
#     print(num1 + num2)
#     print(num1 * num2)

# print(math_ops(20, 10))

# print("=" * 50)

# # processed data
# def process_email(email):
#     print(email.lower() + "@gmail.com")

# print(process_email("KRUpaRao"))

# print("=" * 50)

# # Position Arguements
# def employee_info(emp_name, emp_email, emp_location):
#     print(f"Hi {emp_name} your email is {emp_email} and your address is {emp_location}")

# employee_info("hyderabad", "krupa@gmail.com", "krupa")
# employee_info("krupa", "krupa@gmail.com", "hyderabad")

# print("=" * 50)

# # Keyword Arguements
# def employee_info(emp_name, emp_email, emp_location):
#     print(f"Hi {emp_name} your email is {emp_email} and your address is {emp_location}")

# employee_info("hyderabad", "krupa@gmail.com", "krupa")
# employee_info(emp_location="Hyderabad", emp_name="krupa", emp_email="krupa@gmail.com")

# print("=" * 50)

# # without Default Arguements
# def employee_info(emp_name, emp_email, emp_location, org_name):
#     print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} and your location is {emp_location}")

# employee_info(emp_location="Hyderabad", emp_name="krupa", emp_email="krupa@gmail.com", org_name="IBM")
# employee_info(emp_location="Chennai", emp_name="Nandh", emp_email="nandh@gmail.com", org_name="IBM")

# print("=" * 50)

# # with default arguements
# def employee_info(emp_name, emp_email, emp_location, org_name="IBM"):
#     print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} and your location is {emp_location}")

# employee_info(emp_location="Hyderabad", emp_name="krupa", emp_email="krupa@gmail.com")
# employee_info(emp_location="Chennai", emp_name="Nandh", emp_email="nandh@gmail.com")
# employee_info(emp_location="Nodia", emp_name="Kruparao", emp_email="kruparao@gmail.com", org_name="Infosys")

# print("=" * 50)

# def employee_info(emp_name, emp_email, emp_location, emp_mobile, org_name="IBM", gst="987653726472"):
#     # Non-default argument follows default argument
#     print(f"Hi {emp_name} your email is {emp_email}, mobile number is {emp_mobile} and working for {org_name} and your location is {emp_location}")

# employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com",emp_mobile=999999)

# print("=" * 50)

# # without Arbitrary Positional Arguements
# def add_numbers(num1):
#     print(num1)

# def add_two_numbers(num1, num2):
#     print(num1 + num2)

# def add_five_numbers(n1, n2, n3, n4, n5):
#     print(n1 + n2 + n3 + n4 + n5)

# add_numbers(10)
# add_two_numbers(20,30)
# add_five_numbers(10, 20, 30, 40, 50)

# print("=" * 50)

# # With Arbitrary Positional Arguements
# def add_numbers(*numbers):
#     print(numbers)

# add_numbers(10, 20)
# add_numbers(10, 20, 30)
# add_numbers(10, 20, 30, 40, 50, 60)

# print("=" * 50)

# # with Arbitrary Positional Arguements
# def add_numbers(*numbers):
#     total_sum = 0
#     for sum in numbers:
#         total_sum += sum
#     print(f"Total sum is {total_sum}")

# add_numbers(10, 20, 30, 40, 50, 60)

# print("=" * 50)

# def profile(*info):
#     print(info)

# profile("krupa", "hyderabad", "India")

# print("=" * 50)

# # Real world use case in Ecommerce Cart
# def cart_total_cart(*products):
#     total_cart = 0
#     for price_product in products:
#         total_cart += price_product
#     print(f"Total sum is {total_cart}")

# # Customer One
# cart_total_cart(1250, 2000, 1340, 2300, 3100)
# # Customer Two
# cart_total_cart(1450, 1000, 1340, 1300, 2100)

# print("=" * 50)

# # Arbitrary Keywords
# def profile(**info):
#     print(info)

# profile(first_name="krupa")
# profile(first_name="krupa", last_name="nandh", email="krupa@gmail.com")

# def profile(**info):
#     print(info)

# profile(first_name="Krupa", last_name="nandh", gpa=7.1, passed=True)

# print("=" * 50)

# def profile(**info):
#     for data in info:
#         print(data) # Key

# profile(first_name="Krupa", last_name="nandh", gpa=7.1, passed=True)

# print("=" * 50)

# def profile(**info):
#     for data in info:
#         print(info[data]) # value

# profile(first_name="Krupa", last_name="nandh", gpa=7.1, passed=True)

# print("=" * 50)

# # Real World Use Case -> jan=3000, feb=4500, mar=9000
# # Real World Use Case -> jan=3000, feb=4500, mar=9000, apr=6000, may=3000, jun=5000

# def bank_transaction(**transactions):
#     total_transactions_value = 0
#     total_transactions_count = 0
#     for transaction in transactions:
#         total_transactions_value += transactions[transaction]
#         total_transactions_count += 1
#     print(f"Total transaction is {total_transactions_value} for {total_transactions_count} transactions")

# bank_transaction(jan=3000, feb=4500, mar=9000)
# bank_transaction(jan=3000, feb=4500, mar=9000, apr=6000, may=3000, jun=5000)

# print("=" * 50)

# # with return statement
# def add(a, b):
#     return a + b

# print(add(10, 30))

# # problem statement
# # def add(a, b):
# #     print(a + b) # None

# # # Function Composition
# # def sub(c,d,e): # add c & d, then minus e --> c + d - e 
# #     print(add(c,d)-e) # TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'

# # sub(3,4,5) # 3 + 4 - 5 = 2 (None - 5)

# # Problem Statement
# def add(a,b):
#     return a+b # 7

# # function Composition
# def sub(c,d,e): # add c & d, then minus e --> c + d - e 
#     print(add(c,d)-e)

# sub(5,8,3) # 5 + 8 -3

# print("=" * 50)

# # If you use return, make sure it's the last part of statement to be executed   
# def add(a,b):
#     print("Calculation Started")
#     return a+b 
#     print("Calculation Completed") # Code is structurally unreachable

# print(add(5,5))

# print("=" * 50)

# # If you have multiple return statements, first return will be considered 
# a = 50
# a = 60
# a = 70

# print(a)

# print("=" * 50)

# def math_ops(n1,n2):
#     return n1 + n2
#     return n1 - n2 # Code is structurally unreachable
#     return n1 * n2 # Code is structurally unreachable

# print(math_ops(1,2))

# print("=" * 50)

# def math_ops(n1,n2,operator):
#     if operator == "+":
#         return n1 + n2
#     elif operator == "*":
#         return n1 * n2
#     elif operator == "-":
#         return n1 - n2
#     elif operator == "$":
#         return n1 / n2
#     else:
#         return "Invalid operator given"

# print(math_ops(10,5,"+"))
# print(math_ops(10,5,"*"))
# print(math_ops(10,5,"$"))

# print("=" * 50)

# # Local Scope
# def add():
#     la = 10 # Local - inside the function
#     lb = 20 # Local - inside the function

#     # Accessing within function
#     print(la)
#     print(lb)

# add()

# # accessing outside the function
# # print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?

# # Parameters that we pass to the function, are also local variables
# def add(la,lb):
#     print(la)
#     print(lb)

# add(20,30)

# print("=" * 50)

# # Global Scope
# ga = 100 # Global - Outside the function

# def add(la,lb):
#     print(la)
#     print(lb)
#     print(ga) # Global variables can be accessed inside a function

# add(45,65)
# print(ga) # Global Vriables accessed outside the function

# print("=" * 50)

# # Name Conflicts
# ga = 150 # Global - outside function

# def add(la,lb,ga): # Local - inside the function
#     print(la)
#     print(lb)
#     print(ga) # Local - Accessing inside the function
#     print(globals()['ga']) # Global - Access inside the function

# add(33,46,94)

# print("=" * 50)

# # global variable outside the function
# count = 0
# print(count)
# count += 1
# print(count)

# print("=" * 50)

# # Global variables inside the function
# count = 0
# print(count)

# def increment():
#     global count
#     count += 1
#     return count

# print(increment())

# print("=" * 50)

# # Without Lambda i.e Standard Function
# def add(a,b):
#     return a + b

# print(add(2,3))

# print("=" * 50)

# # WIth Lambda Functions
# # lambda arguements: expression
# lambda a,b:a+b
# # print((lambda_function)(arguements)) # IILE
# print((lambda a, b: a + b)(4, 5))

# print("=" * 50)

# # Without Lambda Function i.e Standard Function
# def is_even_num(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even_num(3))
# print("=" * 50)
# print(is_even_num(6))

# print("=" * 50)

# # WIth Lambda Function
# # lambda arguements: expression
# lambda num: num %2 == 0
# print((lambda num: num % 2 == 0)(4))
# print((lambda num: num % 2 == 0)(7))

# print("=" * 50)

# # Without Higher Order Function 
# # Write a script/program to take a list of numbers and return the square of list of numbers
# # [1,2,3,4,5]   ==>     [1,4,9,16,25]
# def square_list(numbers):
#     squared_list = []
#     for num in numbers:
#         squared_list.append(num * num)
#     return squared_list

# print(square_list([1,2,3,4,5]))

# print("=" * 50)

# # With Higher Order Function - map()
# # Write a script/program to take a list of numbers and return the square of list of numbers
# # [1,2,3,4,5]   ==>     [1,4,9,16,25]
# # map(function, iterable)
# # map(function, [1,2,3,4,5])
# lambda num: num * num
# map((lambda num: num * num),[1,2,3,4,5])
# print(map((lambda num: num * num),[1,2,3,4,5]))
# print(list(map((lambda num: num * num), [1,2,3,4,5]))) # One Liner Function

# print("=" * 50)

# # Real World Use Case Of Working with Lambda & Higher Order Functions 
# products = [
#     {"name": "Laptop", "price": 80000, "discount": 10},
#     {"name": "Phone", "price": 50000, "discount": 5},
#     {"name": "Headphones", "price": 2000, "discount": 15},
#     {"name": "Charger", "price": 1500, "discount": 0},
#     {"name": "Camera", "price": 30000, "discount": 20},

#     {"name": "Tablet", "price": 25000, "discount": 10},
#     {"name": "Monitor", "price": 12000, "discount": 8},
#     {"name": "Keyboard", "price": 2000, "discount": 5},
#     {"name": "Mouse", "price": 1000, "discount": 0},
#     {"name": "Printer", "price": 15000, "discount": 12},

#     {"name": "Smartwatch", "price": 7000, "discount": 18},
#     {"name": "Speaker", "price": 3500, "discount": 10},
#     {"name": "PowerBank", "price": 1800, "discount": 7},
#     {"name": "Router", "price": 2500, "discount": 5},
#     {"name": "HardDisk", "price": 6000, "discount": 15},

#     {"name": "SSD", "price": 5500, "discount": 20},
#     {"name": "Webcam", "price": 2200, "discount": 10},
#     {"name": "Microphone", "price": 3000, "discount": 12},
#     {"name": "Projector", "price": 40000, "discount": 25},
#     {"name": "Drone", "price": 75000, "discount": 30},

#     {"name": "TV", "price": 45000, "discount": 18},
#     {"name": "GamingConsole", "price": 38000, "discount": 15},
#     {"name": "VRHeadset", "price": 20000, "discount": 22},
#     {"name": "GraphicsCard", "price": 65000, "discount": 10},
#     {"name": "Motherboard", "price": 12000, "discount": 8}
# ]

# # Assume In Real World You Have 50k Product Records 
# # Requirement: Give Prices After Applying discounts
# # Implementing Solution Normal Way i.e Imperative Style (How To Do)

# prices_after_discounts = []

# for product in products:
#     print(product)
#     price = product['price']
#     print("Price of Product: ", price)

#     discount = product['discount']
#     print("Discount of the product: ", discount)

#     # Find the price of the product after discount
#     price_after_discount = price - (price * discount / 100)
#     print("Price of product after discount: ", price_after_discount)

#     # Adding/storing Discounted prices
#     prices_after_discounts.append(price_after_discount)

#     print("Prices of products after discount: ", prices_after_discounts)

# print("=" * 50)

# # Assume In Real World You Have 50k Product Records 
# # Requirement: Give Prices After Applying discounts
# # Implementing Solution Using Higher Order Functions i.e Declarative Style (What To Do)

# # print(list(map((lambda num:num * num),[1,2,3,4,5]))) # One Liner Functions
# print(list(map((lambda product:product['price'] - product['price'] * product['discount'] / 100), products)))

# prices_after_discount = list(map((lambda product:product['price'] - product['price'] * product['discount'] / 100), products))
# print("Prices after the Discount: ", prices_after_discount)

# print("=" * 50)

# Real World Use Case Of Working with Lambda & Higher Order Functions 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},

    {"name": "Tablet", "price": 25000, "discount": 10},
    {"name": "Monitor", "price": 12000, "discount": 8},
    {"name": "Keyboard", "price": 2000, "discount": 5},
    {"name": "Mouse", "price": 1000, "discount": 0},
    {"name": "Printer", "price": 15000, "discount": 12},

    {"name": "Smartwatch", "price": 7000, "discount": 18},
    {"name": "Speaker", "price": 3500, "discount": 10},
    {"name": "PowerBank", "price": 1800, "discount": 7},
    {"name": "Router", "price": 2500, "discount": 5},
    {"name": "HardDisk", "price": 6000, "discount": 15},

    {"name": "SSD", "price": 5500, "discount": 20},
    {"name": "Webcam", "price": 2200, "discount": 10},
    {"name": "Microphone", "price": 3000, "discount": 12},
    {"name": "Projector", "price": 40000, "discount": 25},
    {"name": "Drone", "price": 75000, "discount": 30},

    {"name": "TV", "price": 45000, "discount": 18},
    {"name": "GamingConsole", "price": 38000, "discount": 15},
    {"name": "VRHeadset", "price": 20000, "discount": 22},
    {"name": "GraphicsCard", "price": 65000, "discount": 10},
    {"name": "Motherboard", "price": 12000, "discount": 8}
]

# Assume In Real World You Have 50k Product Records 
# Requirement: Find the Premium Products i.e product with price above 25000
# Implementing Solution Normal Way i.e Imperative Style (How To Do)

premium_products = []

for product in products:
    price = product['price']

    if price > 25000:
        print(product)
        premium_products.append(product)

print("Premium Product Collection: ", premium_products)

print("=" * 50)

# Assume In Real World You Have 50k Product Records 
# Requirement: Find the Premium Products i.e product with price above 25000
# Implementing Solution Using Higher Order Functions i.e Declarative Style (What To Do)

# filter(function, iterable)
# filter(function, [1,2,3,4,5,6,7,8,9,10])
# lambda num: num % 2 == 0
print(filter((lambda product: product['price'] > 25000), products))

premium_products = list(filter((lambda product: product['price'] > 25000), products))
print("Premium Products are: ", premium_products)