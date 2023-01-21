#Data Types

#String - That would be something like "Hello World". The code below allows me to pull out a specific character. This is called subscripting. Always start counting with a 0. FYI when numbers are in quotes "123" this is considered a string and not viewed as integers. 
print("Hello" [0])
print("Hello" [1])
print("Hello" [2])
print("Hello" [3])
print("Hello" [4])

#Int - This refers to whole numbers(positive or negative) with NO decimal places. You will write these numbers with no quotes. If you want to write a large number that typically would have commas 123,456,789 you would write it 123_456_789. 
print(123 + 456)

#Float - is numbers with decimals. Think of something like pi 3.14 

#Boolean - It only has two possible value either True or False. Keep note that there are capitals and no quotes. 

#If you want to figure out what type of data something may be you can use the type function. 
num_char = len(input("What is your name? "))
print(type(num_char))

#Before conversion the below line of code will break with a TypeError: can only concatenate str (not "int") to str
# print("Your name has " + num_char + " characters.")
#You can convert the int num_char to a string with the below line of code. After conversion the code now works. .
new_num_char = str(num_char)
print ("Your name has " + new_num_char + " characters.")

a = "123"
print(type(a))
b = 123
print(type(b))

#Even though the 100.5 is written like a string the float in front converts it to a float which can be added to the int 70. 
print(70 + float("100.5"))


#1st challenge of the day
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit + second_digit) 

#Mathematical Operations in Python
3 + 5
7 - 4
3 * 2
# When dividing as below you will always get a float type
6 / 3 
#This is how you do exponets or something raised to the power of.
2 ** 3
#Python follows PEMDAS rules so keep that in mind when working with math. And remember when it comes to * and / and then + and - it works left to right. See the example in the code below.  
print(3 * 3 + 3 / 3 - 3)
#Change the prior code so the answer is 3.0
print(3 * (3 + 3) / 3 - 3)

#Practice two
#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height. Have it return a whole number. 
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
new_height = float(height)
new_weight = float(weight)
BMI = int(new_weight/(new_height ** 2))
str_BMI = str(BMI)
print("Your BMI is " + str_BMI)

#This might be a more straightforward way to write this, if we don't want the "Your BMI is " string included
#bmi = int(weight) / float(height) ** 2
#bmi_as_int = int(bmi)
#print(bmi_as_int)

#After learning about if/else come back and have it return verbiage on BMI class underweight is <18.5, normal is 18.5-25, overwight is 25-30, and obese is >30.

#Number Manipulation and F Strings in Python

#The below code will simply do the math
print(8 / 3)
#However, when you change this to an int it doesn't round it like we would typically expect it just gets rid of the everything including and after the decimal
print(int(8 / 3))
#To actually round this we would do the simple code below. 
print(round(8 / 3))
#You can even be more precise in how many decimal places you want it rounded to. The below code will round it to two decimal places.
print(round(8 / 3, 2))
#This is called floor division and will give the same answer as print(int(8 / 3))
print(8 // 3)

#Takes the previous version of the number and adds one to it. It also works with subtraction, division, and multiplication
score = 0
score += 1
print(score)

#F-string - the f has to go in front of the quotes. This allows you to add all data types together without needing to do all the converting. You must remember to use curly braces around your other data types.
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score} and you are {isWinning} because your height is {height}")

#Practice three
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
age = input("What is your current age? ")
yearsleft = 90 - int(age)
days = yearsleft * 365
weeks = yearsleft * 52
months = yearsleft * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
