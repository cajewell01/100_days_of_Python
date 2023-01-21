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
