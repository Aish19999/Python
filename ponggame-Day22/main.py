import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("Black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)
#timmy = Turtle()
#timmy.color("white")
#timmy.shape("square")
game_is_on=True

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.dowm, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.dowm, "s")


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detecting the collosion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detech collosio with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detech the left paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        ball.reverce_axis()
        scoreboard.l_point()

    # Detech the right paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        ball.reverce_axis()
        scoreboard.r_point()























screen.exitonclick()
