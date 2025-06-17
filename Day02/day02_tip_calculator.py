#Welcome Message
print("Welcome to the tip calculator!")
#User Input
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? 10 12 15? "))
people = int(input("How many people to split the bill? "))

#Tip Calculation: User tip percentage divided by 100 THEN multiplied by the total bill
tip_percent = tip/100
bill_per_percent = tip_percent * bill

#Calculated tip plus the total bill
total_bill = bill_per_percent + bill

#Bill per person and round up to 2 decimal place
bill_per_person = total_bill/people
final_bill = round(bill_per_person, 2)

print(f"Each person should pay: £{final_bill}")



#pay = round((((tip/100) * bill) + bill/people), 2)
#print(pay)