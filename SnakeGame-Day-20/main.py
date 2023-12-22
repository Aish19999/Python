from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

timmy = Turtle()
screen = Screen()
score = Scoreboard()

screen.setup(width =600, height =600)
screen.title("My Snake game")
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #Detect the object collosion
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increment_score()

    #Detect the collosion with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        score.rest_score()
        snake.reset_snake()

    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.rest_score()
            snake.reset_snake()













#timmy.forward(100)



















screen.exitonclick()
