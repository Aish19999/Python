from turtle import Screen, Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            ran_y = random.randint(-250,250)
            new_car.goto(x=300, y= ran_y)
            self.all_car.append(new_car)

    def move_car(self):
        for cars in self.all_car:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed +=MOVE_INCREMENT



