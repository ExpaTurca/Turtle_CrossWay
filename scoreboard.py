from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pen()
        self.level = 1

    def inc_level(self):
        self.level += 1

    def level_board(self):
        self.goto(-280, 250)
        self.clear()
        self.write(f"Level: {self.level}", True, font=FONT)

    def game_over(self):
        self.goto(-60, 0)
        self.clear()
        self.write(f"GAME OVER", True, font=FONT)
        self.goto(-60, 20)
        self.write(f"Score: {self.level}", True, font=FONT)

