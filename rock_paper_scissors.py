rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to Rock, Paper, Scissors!")

personal_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.  "))

print("\n Your Choice: ")
if personal_choice == 0:
  print(rock)
elif personal_choice == 1:
  print(paper)
elif personal_choice == 2:
  print(scissors)

print("\nComputer Choice:")
computer_choice = random.randint(0, 2)
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)

if personal_choice == 0 and computer_choice == 0:
  print("It's a Draw.")
elif personal_choice == 0 and computer_choice == 1:
  print("You Lose.")
elif personal_choice == 0 and computer_choice == 2:
  print("You Win!")
elif personal_choice == 1 and computer_choice == 0:
  print("You Win!")
elif personal_choice == 1 and computer_choice == 1:
  print("It's a Draw.")
elif personal_choice == 1 and computer_choice == 2:
  print("You Lose.")  
elif personal_choice == 2 and computer_choice == 0:
  print("You Lose.")
elif personal_choice == 2 and computer_choice == 1:
  print("You Win!")
elif personal_choice == 2 and computer_choice == 2:
  print("It's a Draw.") 
