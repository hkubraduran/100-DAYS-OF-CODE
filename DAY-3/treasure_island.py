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
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

q1 = input("Do you want to go left or right?\n")
new_q1 = q1.lower()
if  new_q1 == "left" :
  q2 = input("You are in a forest. There is also a lake near the forest. Which option will you choose?\nGo ahead with forest or lake?\n")
  new_q2 = q2.lower()
  if new_q2 == "lake":
    q4 = input("You choose the lake. You have 3 options:\n 1.Across the lake on a broken wooden bridge\n 2.Swim\n 3.Wait the boat to across the lake.\nMake your choice: 1, 2, or 3\n")
    if q4 == "1" :
      print("The wooden steps of the bridge were not strong enough to carry you. You fell into the lake and were eaten by piranhas. Game over...")
    elif q4 == "2":
      print("The piranhas ate you. You choose the wrong option. Game over.")
    elif q4 == "3":
      print("You accross the lake with the boat. Congrats.\n ")
  else :
    q3= input("You face a giant bear. You have two options: 'throw a rock' to the bear or 'run away'. Make your choice.\n")
    new_q3 = q3.lower() 
    if new_q3 == "throw a rock":
      print("You pissed off the bear. You are dead. Game over... ")
    elif new_q3 == "run away" :
      print("You make noise while running away and the bear noticed you. You are dead. Game over...")
    else :
      print("There is no way to run away and get rid off a bear. You made your choice. You are dead. Game over...")
else :
  print("Fall into a hole with a lot of snake. You have bitten. Game over...")
  