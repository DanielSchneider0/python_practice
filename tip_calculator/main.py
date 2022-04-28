# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to Split bill calculator")

total_bill = float(input("What is the total bill? "))
tip_percentage = int(input("What percentage do you want to tip? "))
party_total = int(input("How many people are splitting the bill? "))

convert_tip_to_percent = tip_percentage / 100

with_tip = (total_bill * convert_tip_to_percent) + total_bill

split_with_tip = with_tip / party_total

final_amount = "{:.2f}".format(split_with_tip)

print(f"Each person owes ${final_amount}.")
