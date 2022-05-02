import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player_choice = input("Rock, Paper, or scissor?\n").lower()


if player_choice == "paper":
    print(paper)
elif player_choice == "rock":
    print(rock)
elif player_choice == "scissor":
    print(scissors)

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if (
    player_choice == "rock"
    and computer_choice == 2
    or player_choice == "scissor"
    and computer_choice == 1
):
    print("Player 1 Wins")
elif player_choice == "paper" and computer_choice == 0:
    print("player 1 wins!")
elif player_choice == "rock" and computer_choice == 1:
    print("Computer Wins!")
elif player_choice == "scissor" and computer_choice == 0:
    print("computer wins!")
elif player_choice == "paper" and computer_choice == 2:
    print("Computer Wins")
else:
    print("Its a tie, play again.")
