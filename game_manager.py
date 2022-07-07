import random

from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


class GameManager:
    def __init__(self):
        self.screen = Screen()
        self.score = Scoreboard()
        self.game_is_on = True
        self.score.level_board()
        self.cars = []

    def spawn_car(self):
        new_car = CarManager()
        self.cars.append(new_car)
        new_x = random.randint(250, 280)
        new_y = random.randint(-260, 260)
        new_car.goto(new_x, new_y)

    def next_level(self, actor):
        for local in self.cars:
            local.level += 1
        actor.reset_actor()
        self.score.inc_level()
        self.score.level_board()

    def is_game_over(self):
        return not self.game_is_on

    def game_over(self, condition):
        if condition == "true":
            print(f"game is: {self.game_is_on}")
            self.game_is_on = False
            self.score.game_over()
        return self.game_is_on
