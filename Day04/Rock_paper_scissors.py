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
#List for rock, paper, scissors variables
game = [rock, paper, scissors]

#List for name of the Variable
choices_name = ["rock", "paper", "scissors"]

#Welcome message and player input
print("Welcome to Rock, Paper, Scissors Game")
player = int(input("What will you pick?\nType 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(f"Player Choice is: {choices_name[player]}")

#Conditional to avoid player value error
if player >= 0 and player <= 2:
    print(game[player])
else:
     print("Incorrect input\nPlease enter the correct one")

#Randomization for computer output
computer_random = random.randint(0,2)
print(f"Computer choose: {choices_name[computer_random]}")
print(game[computer_random])



if computer_random == 0 and player == 2:
    print("Computer Won")
elif computer_random == 2 and player == 1:
    print("Computer Won")
elif computer_random == 1 and player == 0:
    print("Computer Won")
elif computer_random == player:
    print("It's a Tie")
else:
    print("Player Won")



