#Write a calculator that figures out what each person should pay if the bill was $150.00, split between 5 people, with 12% tip. 
#Format the result to 2 decimal places

print("Welcome to the Tip Calculator!")
total = input("What was the total of the bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
numberofpeople = input("How many people to split the bill? ")
tipAmount = float(total) * (int(tip)/100)
finalTotal = float(total) + tipAmount
splitTotal = finalTotal / int(numberofpeople)
splitTotal = format(splitTotal, '.2f')
print(f"Each person should pay: ${splitTotal}")

#The '.2f' is what formats the result to two decimal places. 


#This code below is not my own, it belongs to the instructor. I saved it for learning purposes.
print("Welcome to the Tip Calculator!")
total = float(input("What was the total of the bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
