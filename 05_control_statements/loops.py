# Looping Structures (Iteration Statements) (Repitition)

# While Loop

while False:
    print("Repeat...")
    print("Code........")

# while True: # This Forms an infinite loop
#    print("Repeat...")
#    print("Code.........")

# To stop Above infinite loop press  control + c

# counters
count = 1
while count <= 5:
    print("Count Is: ", count)
    count += 1

print("===========================")

# Requirement: Generate Empmloyee ID's 10001 - 15000
# emp_id = 10001
# while emp_id <= 15000:
#     print("Employee ID Generated: ", emp_id)
#     emp_id += 1

print("============================")

# we use while loop, when we don't know
# Number of Iterations / Repetitions In Advance

# You Found A lost phone, Trying To Break PIN / Password
# Tell me at which attempt, The Phone will be unclocked?

# actual_pin = "2345"
# user_entered_pin = ""

# while user_entered_pin != actual_pin:
#     user_entered_pin = input("Enter PIN to unclock: ")
# print("Phone Unclocked")

print("============================")

# for loop
prices_products = [1000,1500,2000,2500,3000,10000]

# Requirement: Some offer is runnning -> Provide a discount of 250 on each product
# In Lists We Have Index, which starts from Zero and Keeps Increasing
# Without for loop
print("======== Prices Before Discount ========")
print(prices_products[0])
print(prices_products[1])
print(prices_products[2])
print(prices_products[3])
print(prices_products[4])
# print(prices_products[5])
# print(prices_products[.])
# print(prices_products[.])

print("======== Prices After Discount ========")
print(prices_products[0] - 250)
print(prices_products[1] - 250)
print(prices_products[2] - 250)
print(prices_products[3] - 250)
print(prices_products[4] - 250)
# print(prices_products[5] - 250)
# print(prices_products[.] - 250)
# print(prices_products[.] - 250)

# with for loop
prices_products = [1000,1500,2000,2500,3000,3500,4000,4500,5000]
print("======== Prices Before Discount ========")
for price in prices_products:
    print("Price of product Before discount: ", price)

print("======== Prices After Discount ========")
for price in prices_products:
    print("Price of product After Discount: ", price - 250)

print("============================")
# range() function
# range(start, stop, step)

for num in range(6):
    print(num)

for num in range(0, 11, 1):
    print(num)

print("=====================")

for emp_id in range(10001,10101,1):
    print("Employee ID generated: ", emp_id)

print("=====================")

# prices_products = [1000,1500,2000,2500,3000,3500,4000,4500,5000,100000]
for price_product in range(1000,50500,500):
    print("Price of product: ", price_product)

print("=====================")

for num in range(1,11,1):
    print(num)

for num in range(10,0,-1):
    print(num)