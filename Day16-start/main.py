import turtle
import prettytable

# Construct object from the Blue print
timmy = turtle.Turtle()
print(f"Timmy : {timmy}")
timmy.shape("turtle")
timmy.color("red")
timmy.screen.title('Object-oriented turtle demo')
timmy.screen.bgcolor("orange")
timmy.forward(100)

# Method 2nd

# from turtle import Turtle, Screen

# gimmy = Turtle()
# print(f"Gimmy: {gimmy}")

# Object attribute
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitoncick()

########################## Pretty Table
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokeman Name", "Type"]
table.add_row(["Pekachu", "Electric"])
table.add_row(["Squrtile", "Water"])
table.add_row(["Charmander", "Fire"])

table.align = "l"

print(table)
