from turtle import Turtle, Screen
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Games")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#Get the coordinates of the mouse click
# def get_mouse_coordinates(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_coordinates)
# turtle.mainloop()

ans_state = screen.textinput(title="Guess the state", prompt="What's another state's names")






















screen.exitonclick()
