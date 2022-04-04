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

print("You find yourself on a path through the woods. You reach a fork in the road.")
choice1 = input("Do you go left, right, or straight? ")
if choice1 == "left":
    print("You come upon a small dark house. It is dark inside. Suddenly you hear a growl, right before you are eaten by a grue. Game Over. ")
elif choice1 == "right":
    choice3 = input("You come upon a lake. Do you attempt to swim, take the ferry across, or follow the path? ")
    if choice3 == "swim":
        print("The water is exceptionally cold and murky. Suddenly, the jaws of the lake monster clamp around you. Game Over.")
    elif choice3 == "ferry":
        choice4 = input("You take the ferry across the lake. On the other shore you see a path forward or to the left. Which way? ")
        if choice4 == "forward":
            print("You enter a clearing. In front of you is a hoard of glittering treasure. You WIN!")
        elif choice4 == "left":
            print("You enter a small clearing. You hear rustling in the bushes and growling before a giant bear rips you to shreds. Game Over.")
elif choice1 == "straight":
    print("You enter a small clearing. You hear rustling in the bushes and growling before a giant bear rips you to shreds. Game Over.")
