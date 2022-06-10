# import module

# print(module.variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.color("DarkGreen")

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Mew", "Squirtle"])
table.add_column("Type", ["Electric", "Magic", "Water"])
table.align = "l"
print(table)
