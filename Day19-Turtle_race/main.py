from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title ="Make your bet", prompt="Which turtle will win the race? Enter the color?")
col = ["purple", "blue", "yellow", "green", "red", "orange"]
all_turtle = []
is_race_on = True
x= -230
y= 80
for racer in range(0,6):
        new_turtle = Turtle(shape = "turtle")
        new_turtle.color(col[racer])
        new_turtle.penup()
        new_turtle.goto(x,y)
        new_turtle.back(10)
        y= y-30
        all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for n in all_turtle:
        if n.xcor() > 230:
            is_race_on = False
            winner = n.pencolor()
            if winner == user_bet:
                print(f"You won! the winner is {winner}")
            else:
                print(f"You lose! the winner is {winner}")

        distance = random.randint(0,10)
        n.forward(distance)


screen.exitonclick()



