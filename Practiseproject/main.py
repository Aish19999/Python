from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Snake game")
screen.tracer()

snake = Snake()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.up, "UP")














screen.exitonclick()