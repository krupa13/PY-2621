# Nested Conditions

# inner conditions is only checked if the outer condition is true

if True:
    print("One")
if True:
    print("This is NOT Nested condition")

if True: # Outer Condition
    print("1")
    if True: # Inner Condition
        print("This is Nested Condition")

# Nested Condition Use Case
age = int(input("Enter your Age: "))
if age >= 18:
    has_id = input("Do you Have ID (Yes/No): ")
    if has_id == "yes":
        print("You can vote")
    else:
        print("You cannot vote without ID proof")
else:
    print("you cannot vote with Under age.")