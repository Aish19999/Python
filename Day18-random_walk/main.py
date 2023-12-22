from turtle import Turtle, Screen
#from turtle import *
import random
screen = Screen()
timmy = Turtle()
direction = ['0', '90','180','270']
screen.colormode(255)
timmy.pensize(15)
timmy.speed("fast")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_col = (r, g, b)
    return random_col

colour = [random_color]
print(colour)
for n in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(float(random.choice(direction)))


screen.exitonclick()


















screen = Screen()
screen.exitonclick()