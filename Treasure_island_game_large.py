print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. \n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You are shipwrecked on an island and while searching for supplies you stumble across a treasure map.")
begin = input("Would you like to search for treasure? Y or N. \n")

if (begin == "Y") or (begin == "y"):
  print("After looking at the map you determine the X is directly north of your location. You look around and notice an old path leading through the dense jungle or a newer path that seems to be cleared. \n")
  path = input("Do you take the jungle path or the cleared path? ")
  if path == "Jungle" or path == "jungle":
    print("The jungle is a dense maze and you worry you have made the wrong choice. A leopard suddenly emerges from the jungle and is blocking you from continuing north \n")
    leopard = input("What do you do? Wait, move closer, or run. ")
    if leopard == "wait" or leopard == "Wait":
      print("You choose to wait patiently to see if he will move. The leopard looks you up and down for a few minutes before deciding that you mean no harm and he disappears back into the jungle. \n")
      print("You continue on your journey and arrive at a cave. This seems to be place the map has indicated the treasure will be. \n")
      continue_journey = input("Do you explore the outside of the cave or the inside of the cave first? ")
      if continue_journey == "outside" or continue_journey == "Outside":
        print("You begin exploring all around outside of the cave. It is during this exploriation that you notice there is a second entrance to this cave that is densly covered by vines and other plants. \n")
        which_cave_entrance = input("What cave entrance do you choose? The original or the new? ")
        if which_cave_entrance == "original" or which_cave_entrance == "Original":
          print("You walk back to the main entrance. You enter the cave and see that the path inside of the cave splits to the left and to the right. \n")
          cave_path = input("What path do you take? The left or the right. ")
          if cave_path == "left" or cave_path == "Left":
            print("The path is long and straight. You wonder if you will ever come to the end of it. The path is going lower into the belly of the cave. It becomes colder and more damp. Finally you arrive at a big opening and you can see the chest in the center, so you move towards it. When you arrive at the chest you see a note to the right. You pick it up and begin to read it. The note reads 'Only one number between 1 and 10 will open me. All other numbers will lead to certain death.' \n")
            number_choice = int(input("What number do you pick? "))
            if number_choice == 8:
              print("You have opened the treasure chest! There is another note inside which gives you the details on the location of enough supplies to last until you are rescued.")
            elif number_choice <=7:
              print("You hear a noise in the distance, but you are unable to determine what is was before you are hit with a poison dart that kills you.")
            else:
              print("The cave begins to shake and rocks tumble down blocking the ways to leave. You slowly die from the cold and lack of food and water.")
          elif cave_path == "right" or cave_path == "Right":
            print("You have walked right into a booby trap and never make it out of the cave alive!")
        elif which_cave_entrance == "new" or which_cave_entrance == "New":
          print("You enter the newly found entrance and notice stairs in front of you. You decide to follow them and soon you arrive at a big opening and you can see the chest in the center, so you move towards it. When you arrive at the chest you see a note to the right. You pick it up and begin to read it. The note reads 'Only one number between 1 and 10 will open me. All other numbers will lead to certain death.' \n")
          number_choice = int(input("What number do you pick? "))
          if number_choice == 8:
            print("You have opened the treasure chest! There is another note inside which gives you the details on the location of enough supplies to last until you are rescued.")
          elif number_choice <=7:
            print("You hear a noise in the distance, but you are unable to determine what is was before you are hit with a poison dart that kills you.")
          else:
              print("The cave begins to shake and rocks tumble down blocking the ways to leave. You slowly die from the cold and lack of food and water.")
      elif continue_journey == "inside" or continue_journey == "Inside":
        print("You enter the cave and see that the path inside of the cave splits to the left and to the right. \n")
        cave_path = input("What path do you take? The left or the right. ")
        if cave_path == "left" or cave_path == "Left":
          print("The path is long and straight. You wonder if you will ever come to the end of it. The path is going lower into the belly of the cave. It becomes colder and more damp. Finally you arrive at a big opening and you can see the chest in the center, so you move towards it. When you arrive at the chest you see a note to the right. You pick it up and begin to read it. The note reads 'Only one number between 1 and 10 will open me. All other numbers will lead to certain death.' \n")
          number_choice = int(input("What number do you pick? "))
          if number_choice == 8:
            print("You have opened the treasure chest! There is another note inside which gives you the details on the location of enough supplies to last until you are rescued.")
          elif number_choice <=7:
            print("You hear a noise in the distance, but you are unable to determine what is was before you are hit with a poison dart that kills you.")
          else:
            print("The cave begins to shake and rocks tumble down blocking the ways to leave. You slowly die from the cold and lack of food and water.")
        elif cave_path == "right" or cave_path == "Right":
          print("You have walked right into a booby trap and never make it out of the cave alive!")
    elif leopard == "move closer" or leopard == "Move Closer" or leopard =="Move closer" or leopard == "move Closer":
      print("You slowly start to inch forward hoping that he will run, but he doesn't seem to move. All of a sudden he charges at you. \n")
      leopard_attack = input("What do you do? Yell or run. ")
      if leopard_attack == "yell" or leopard_attack == "Yell":
        print("You decided to yell at the attacking leopard. He gets scared and runs off into the jungle. For now you are safe. \n")
        print("You continue on your journey and arrive at a cave. This seems to be place the map has indicated the treasure will be. \n")
        continue_journey = input("Do you explore the outside of the cave or the inside of the cave first? ")
        if continue_journey == "outside" or continue_journey == "Outside":
          print("You begin exploring all around outside of the cave. It is during this exploriation that you notice there is a second entrance to this cave that is densly covered by vines and other plants. \n")
          which_cave_entrance = input("What cave entrance do you choose? The original or the new? ")
          if which_cave_entrance == "original" or which_cave_entrance == "Original":
            print("You walk back to the main entrance. You enter the cave and see that the path inside of the cave splits to the left and to the right. \n")
            cave_path = input("What path do you take? The left or the right. ")
            if cave_path == "left" or cave_path == "Left":
              print("The path is long and straight. You wonder if you will ever come to the end of it. The path is going lower into the belly of the cave. It becomes colder and more damp. Finally you arrive at a big opening and you can see the chest in the center, so you move towards it. When you arrive at the chest you see a note to the right. You pick it up and begin to read it. The note reads 'Only one number between 1 and 10 will open me. All other numbers will lead to certain death.' \n")
              number_choice = int(input("What number do you pick? "))
              if number_choice == 8:
                print("You have opened the treasure chest! There is another note inside which gives you the details on the location of enough supplies to last until you are rescued.")
              elif number_choice <=7:
                print("You hear a noise in the distance, but you are unable to determine what is was before you are hit with a poison dart that kills you.")
              else:
                print("The cave begins to shake and rocks tumble down blocking the ways to leave. You slowly die from the cold and lack of food and water.")
            elif cave_path == "right" or cave_path == "Right":
              print("You have walked right into a booby trap and never make it out of the cave alive!")
          elif which_cave_entrance == "new" or which_cave_entrance == "New":
            print("You enter the newly found entrance and notice stairs in front of you. You decide to follow them and soon you arrive at a big opening and you can see the chest in the center, so you move towards it. When you arrive at the chest you see a note to the right. You pick it up and begin to read it. The note reads 'Only one number between 1 and 10 will open me. All other numbers will lead to certain death.' \n")
            number_choice = int(input("What number do you pick? "))
            if number_choice == 8:
              print("You have opened the treasure chest! There is another note inside which gives you the details on the location of enough supplies to last until you are rescued.")
            elif number_choice <=7:
              print("You hear a noise in the distance, but you are unable to determine what is was before you are hit with a poison dart that kills you.")
            else:
                print("The cave begins to shake and rocks tumble down blocking the ways to leave. You slowly die from the cold and lack of food and water.")
        elif continue_journey == "inside" or continue_journey == "Inside":
          print("You enter the cave and see that the path inside of the cave splits to the left and to the right. \n")
          cave_path = input("What path do you take? The left or the right. ")
          if cave_path == "left" or cave_path == "Left":
            print("The path is long and straight. You wonder if you will ever come to the end of it. The path is going lower into the belly of the cave. It becomes colder and more damp. Finally you arrive at a big opening and you can see the chest in the center, so you move towards it. When you arrive at the chest you see a note to the right. You pick it up and begin to read it. The note reads 'Only one number between 1 and 10 will open me. All other numbers will lead to certain death.' \n")
            number_choice = int(input("What number do you pick? "))
            if number_choice == 8:
              print("You have opened the treasure chest! There is another note inside which gives you the details on the location of enough supplies to last until you are rescued.")
            elif number_choice <=7:
              print("You hear a noise in the distance, but you are unable to determine what is was before you are hit with a poison dart that kills you.")
            else:
              print("The cave begins to shake and rocks tumble down blocking the ways to leave. You slowly die from the cold and lack of food and water.")
          elif cave_path == "right" or cave_path == "Right":
            print("You have walked right into a booby trap and never make it out of the cave alive!")              
    else:
      print("Once you have turned your back, the leopard views you as prey. He quickly catches you and makes you his dinner.")    
        
  elif path == "Cleared" or path == "cleared":
    print("You start walking along the path and as you do, you wonder you has cleared this path. Was it the person who left the treasure or someone else. Suddenly you notice a pirate standing in front of you. Now you know who created this path. \n")
    native_choice = input("Do you talk to or run from the person in front of you? ")
    if native_choice == "talk" or native_choice =="Talk" or native_choice == "Talk to" or native_choice == "talk to":
      print("You thought trying to talk to the pirate would help. However, it gave the pirate enough time to react to an invader on his island. He shoots his pistol at you and you fall to the ground, dead.")
    elif native_choice == "run" or native_choice == "Run":
      print("You catch the pirate off guard and you run so fast and so far you think you are lost. When you finally look up. you realize you have made it to a cave. The map indicates that this cave is where you will find the treasure. \n")
      continue_journey = input("Do you explore the outside of the cave or the inside of the cave first? ")
      if continue_journey == "outside" or continue_journey == "Outside":
        print("You begin exploring all around outside of the cave. It is during this exploriation that you notice there is a second entrance to this cave that is densly covered by vines and other plants. \n")
        which_cave_entrance = input("What cave entrance do you choose? The original or the new? ")
        if which_cave_entrance == "original" or which_cave_entrance == "Original":
          print("You walk back to the main entrance. You enter the cave and see that the path inside of the cave splits to the left and to the right. \n")
          cave_path = input("What path do you take? The left or the right. ")
          if cave_path == "left" or cave_path == "Left":
            print("The path is long and straight. You wonder if you will ever come to the end of it. The path is going lower into the belly of the cave. It becomes colder and more damp. Finally you arrive at a big opening and you can see the chest in the center, so you move towards it. When you arrive at the chest you see a note to the right. You pick it up and begin to read it. The note reads 'Only one number between 1 and 10 will open me. All other numbers will lead to certain death.' \n")
            number_choice = int(input("What number do you pick? "))
            if number_choice == 8:
              print("You have opened the treasure chest! There is another note inside which gives you the details on the location of enough supplies to last until you are rescued.")
            elif number_choice <=7:
              print("You hear a noise in the distance, but you are unable to determine what is was before you are hit with a poison dart that kills you.")
            else:
              print("The cave begins to shake and rocks tumble down blocking the ways to leave. You slowly die from the cold and lack of food and water.")
          elif cave_path == "right" or cave_path == "Right":
            print("You have walked right into a booby trap and never make it out of the cave alive!")
        elif which_cave_entrance == "new" or which_cave_entrance == "New":
          print("You enter the newly found entrance and notice stairs in front of you. You decide to follow them and soon you arrive at a big opening and you can see the chest in the center, so you move towards it. When you arrive at the chest you see a note to the right. You pick it up and begin to read it. The note reads 'Only one number between 1 and 10 will open me. All other numbers will lead to certain death.' \n")
          number_choice = int(input("What number do you pick? "))
          if number_choice == 8:
            print("You have opened the treasure chest! There is another note inside which gives you the details on the location of enough supplies to last until you are rescued.")
          elif number_choice <=7:
            print("You hear a noise in the distance, but you are unable to determine what is was before you are hit with a poison dart that kills you.")
          else:
              print("The cave begins to shake and rocks tumble down blocking the ways to leave. You slowly die from the cold and lack of food and water.")
      elif continue_journey == "inside" or continue_journey == "Inside":
        print("You enter the cave and see that the path inside of the cave splits to the left and to the right. \n")
        cave_path = input("What path do you take? The left or the right. ")
        if cave_path == "left" or cave_path == "Left":
          print("The path is long and straight. You wonder if you will ever come to the end of it. The path is going lower into the belly of the cave. It becomes colder and more damp. Finally you arrive at a big opening and you can see the chest in the center, so you move towards it. When you arrive at the chest you see a note to the right. You pick it up and begin to read it. The note reads 'Only one number between 1 and 10 will open me. All other numbers will lead to certain death.' \n")
          number_choice = int(input("What number do you pick? "))
          if number_choice == 8:
            print("You have opened the treasure chest! There is another note inside which gives you the details on the location of enough supplies to last until you are rescued.")
          elif number_choice <=7:
            print("You hear a noise in the distance, but you are unable to determine what is was before you are hit with a poison dart that kills you.")
          else:
            print("The cave begins to shake and rocks tumble down blocking the ways to leave. You slowly die from the cold and lack of food and water.")
        elif cave_path == "right" or cave_path == "Right":
            print("You have walked right into a booby trap and never make it out of the cave alive!")    
else:
  print("You never make it off the island alive :( ")
