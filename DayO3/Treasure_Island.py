print(r'''
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
/______/______/______/______/______/______/______/______/______/______/[DETIOSA]
*******************************************************************************
''')
#Introductory Message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#First scenario - DIRECTIONAL CHOICE
print("You've hit your first crossroad. Where do you want to go hunter?")
direction = input('Choose a direction: "Left" or "Right"? ').lower()

if direction == "left":
    print("You found yourself in a beach.\nThere is a beautiful Island with a small hut "
          "in the middle")
    movement = input('Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
#second scenario - WAIT OR SWIM CHOICE
    if movement == "wait":
        print("You arrived at the island unharmed.\nThe hut has 3 doors with different colors.")
        doors = input("One red, one yellow and one blue. Which colour do you choose? ").lower()
#Third Scenario - DOOR CHOICE
        if doors == "red":
            print("You entered a burning room. Game Over")
        elif doors == "yellow":
            print("Congratulations\nYou found the TREASURE CHEST.\nYou Win")
#GAME OVER
        else:
            print("You entered a room full of sharks. Game Over")

    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell in a large hole.")
    print("Game Over.")


