from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score =0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(30, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align="right", font=("Arial", 24, "normal"))

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def rest_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('data.txt', mode ='w') as file:
            file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over", align="center", font=("Arial", 24, "normal"))



