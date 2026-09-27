# Simple EMI calculator of a car

onroad_price = 880516
down_payment = 88000
bank_interest_rate = 8.9
loan_years = 4

#Calculating the loan amount
loan_amount = onroad_price - down_payment

# convert the yearly interest rate to monthly interest rat
monthly_emi_interest_rate = bank_interest_rate / 100 / 12

# convert loan years to month
months = loan_years * 12

# calculate the EMI
# emi formula P * R * (1 + R)^N / (1 + R)^N - 1
# P = Principle amount (loan amount), R = Rate of Interest (monthly emi interest)
# N = Number of months

emi = loan_amount * monthly_emi_interest_rate * (1 + monthly_emi_interest_rate) ** months
emi = emi / ((1 + monthly_emi_interest_rate) ** months - 1)

# total amount payable
total_amount = emi * months

print("On Road Amount of the Car: ₹", round(onroad_price))
print("Down payment: ₹", round(down_payment))
print("Bank Interest Rate: ", bank_interest_rate)
print("Loan Period: ", loan_years)
print("Total Loan Amount: ₹", round(loan_amount))
print("Total Amount to be Paid: ₹", round(total_amount))
print("EMI per month to be paid: ₹", round(emi))