import turtle
from turtle import Turtle,Screen
import pandas

screen = Screen()
screen.title("The US state game")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

is_game_on = True
score =0

while is_game_on and score < 50:
    ans_state = screen.textinput(title=f"Guess the state {score}", prompt="What's the another state").title()

    if ans_state == "Exit":
        break

    data = pandas.read_csv("50_states.csv")
    print(data)
    state = data["state"].tolist()
    print(state)
    if ans_state in state:
       t = Turtle()
       t.hideturtle()
       t.penup()
       state_data = data[data.state == ans_state]
       t.goto(int(state_data.x), int(state_data.y))
       t.write(ans_state)
       score +=1

























screen.exitonclick()





















screen.exitonclick()

