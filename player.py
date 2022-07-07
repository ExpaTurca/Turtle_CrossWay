from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COOLDOWN = 1


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.setheading(90)
        self.cooldown = COOLDOWN
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(10)

    def reset_actor(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def car_crash(self, cars):
        for car in cars:
            if (self.distance(car.position()) < 10 and self.ycor() == car.ycor() - 10) or \
                    (self.distance(car.position()) < 15 and self.xcor() == car.xcor()):
                return True
        return False
