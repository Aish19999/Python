from turtle import Turtle, Screen

POSITION =[(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE =20
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segment = []
        self.head = self.segment[0]
        self.create_snake()

    def create_snake(self):
        for pos in POSITION:
            seg = Turtle()
            seg.shape("square")
            seg.color("white")
            seg.penup()
            seg.goto(pos)

    def move(self):
        for n in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[n -1].xcor()
            new_y = self.segment[n - 1].ycor()
            self.segment[n].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)



