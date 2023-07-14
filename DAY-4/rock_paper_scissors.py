import random
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
game_visuals = [rock, paper, scissors]
players_turn = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
#print player's choice
if players_turn < 0 or players_turn >= 3:
  print("Invalid number")
else:
  print(game_visuals[players_turn])
  computers_turn = random.randint(0, 2)
  print("Computer choose:")
  print(game_visuals[computers_turn])
  
  players_choice = str(players_turn)
  computers_choice = str(computers_turn)
  #check the winner
  if players_choice == "0": #rock
    if computers_choice == "1":
      print("You lose.")
    elif computers_choice == "0":
      print("There is no winner.")
    else :
      print("You win.")
  
  elif players_choice == "1": #paper
    if computers_choice == "0":
      print("You win.")
    elif computers_choice == "1":
      print("There is no winner.")
    else :
      print("You lose.")
  
  else:  #players_turn == 2 (scissors)
    if computers_choice == "0":
      print("You lose.")
    elif computers_choice == "1":
      print("You win.")
    else :
      print("There is no winner.")