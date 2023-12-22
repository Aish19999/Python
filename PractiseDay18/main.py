from turtle import Turtle, Screen
import random

timmy = Turtle()

#Drawing the dash line
#for n in range(0,50):
#    timmy.forward(10)
#    timmy.pendown()
#    timmy.forward(10)
#    timmy.penup()

#Drwaing different shapes

# def draw_shapes(num_sides):
#     angle = (360 / num_sides)
#     for n in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for n in range(3,11):
#     draw_shapes(n)

#Random Walk
# import random
# direction = ['0','90','180','270']
# timmy.pensize(10)
# color = ['violet','blue','green','red','pink','yellow','orange']
#
# for n in range(200):
#     timmy.forward(30)
#     timmy.color(random.choice(color))
#     timmy.setheading(float(random.choice(direction)))

#Use the Random RGB color to genearte a random walk
# screen = Screen()
# screen.colormode(255)
#
# direction = ['0','90','180','270']
# timmy.pensize(10)
#
# def random_tuple():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_tuple = (r, g, b)
#     return random_tuple
#
# for n in range(200):
#     timmy.color(random_tuple())
#     timmy.forward(30)
#     timmy.setheading(float(random.choice(direction)))
#     timmy.forward(30)
#
# screen.exitonclick()

# #Spiral circle
# screen = Screen()
# screen.colormode(255)
#
# def random_tuple():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# timmy.speed('fastest')
# #print(timmy.heading())
# def draw(size_gap):
#     for _ in range(int(360/size_gap)):
#         col = random_tuple()
#         timmy.color(col)
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_gap)
#
# draw(5)
# screen.exitonclick()
screen = Screen()

def move_forward():
    timmy.forward(100)
def move_back():
    timmy.right(180)
    timmy.forward(100)

def move_clockwise():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def move_anticlockwise()  :
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

screen.listen()
screen.onkey( key ="W", fun= move_forward)
screen.onkey(key="B", fun=move_back)
screen.onkey(key="A", fun=move_clockwise)
screen.onkey(key="D", fun=move_anticlockwise)





screen.exitonclick()