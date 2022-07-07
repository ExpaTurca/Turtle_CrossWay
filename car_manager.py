import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEVEL = 1


class CarManager(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.move_speed = MOVE_INCREMENT
        self.penup()
        self.level = LEVEL

    def move(self):
        self.forward(self.move_speed)

    def stop(self):
        self.forward(0)

    def inc_speed(self):
        print(self.move_speed)
        self.move_speed += self.level

    def change_color(self):
        self.color(random.choice(COLORS))
