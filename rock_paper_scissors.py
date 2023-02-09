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
game_images = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissors!")

personal_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.  "))
print("\nYour Choice: ")
if personal_choice >= 3 or personal_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[personal_choice])

    print("\nComputer Choice:")
    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])

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

#This is how the instructor did her code. I wanted to save it because the logic is less code than mine
    #if personal_choice >= 3 or personal_choice < 0:
        #print("You typed an invalid number, you lose!")
    #elif personal_choice == 0 and computer_choice == 2:
        #print("You Win!")
    #elif computer_choice == 0 and personal_choice ==2:
        #print("You Lose.")
    #elif computer_choice > personal_choice:
        #print("You Lose.")
    #elif personal_choice > computer_choice:
        #print("You Win!")
