from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

colours =['blue', 'red', 'green', 'orange', 'yellow', 'pink', 'violet','DarkOrchid']

def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    for n in range (0,num_of_sides ):
        timmy.forward(100)
        timmy.right(angle)

for a in range(3,11):
    timmy.color(random.choice(colours))
    draw_shape(a)


































screen = Screen()
screen.exitonclick()

