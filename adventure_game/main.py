print(
    '''
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
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input(
    'You\'re at a cross road. Where do you want to go? type "left" or "right".\n'
).lower()


if choice_1 == "left":
    choice2 = input(
        "You arrive at a lake. There is an island in the middle of the lake. Type 'wait' for a boat. Type 'swim' to swim across.\n"
    ).lower()
    if choice2 == "wait":
        choice_3 = input(
            "You arrived to the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n"
        ).lower()
        if choice_3 == "red":
            print("Game over, You were burned by fire in door one.")
        elif choice_3 == "yellow":
            print("Winner, you found the Treasure!")
        elif choice_3 == "blue":
            print("Game over! You fell into a pit of water.")
        else:
            print("Game Over. You chose a door that doesn't exist.")
    else:
        print("Game Over. You got eaten by a shark.")
else:
    print("Game Over! You went the wrong way")
