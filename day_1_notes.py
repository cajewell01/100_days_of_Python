# Write your code below this line 👇
print("Hello world")

# The \n with NO spaces makes this cut into two lines
print ("I love Laura!\nForever and ever!")

# using the pound sign will make something comment which doesn't print. You can also do this easily using command / on a mac
#input() will get user input in console
#Then print() will print the word "Hello and the user input"
print("Hello " + input("What is your name? "))

# This is going to print the length of the name that is input
print(len(input("What is your name ")))

# We are now storing the input into a variable that we put out front with an equal sign after
# It is IMPORTANT to note that if you use the variable name again it will rewrite to the most recent version
name = input("What is your name? ")
print("My name is " + name)
name = "Jack"
print("My name is " + name)

# We can do the same thing as the code on line 13 by using variables
name = input("What is your name? ")
length = len(name)
print(length)

# Write a program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

# Make your code readable. Make sure you choose variable names that make sense even if you come back a year later. If you want to use user name as a variable you need to use and underscore like - user_name. Also do not name a variable the same as a function like - input. Numbers can be used in the variable name, but they can NOT be at the beginning of the name. 