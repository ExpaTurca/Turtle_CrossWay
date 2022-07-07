import random
import time
from turtle import Screen
from game_manager import GameManager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_is_on = False
cars = []

actor = Player()
game = GameManager()
screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(actor.move, "w")


def spawn_car():
    game.new_car = CarManager()
    cars.append(game.new_car)
    new_x = random.randint(250, 280)
    new_y = random.randint(-250, 250)
    game.new_car.goto(new_x, new_y)


if not game.is_game_over():
    game_is_on = True

cooldown = 3
while game_is_on:
    time.sleep(0.1)
    if cooldown > 0:
        cooldown -= 0.2
    elif cooldown <= 0:
        game.spawn_car()
        cooldown = 1

    for local in game.cars:
        local.move()
        if actor.finish_line():
            game.next_level(actor)
    if actor.car_crash(cars):
        game.game_over("true")

    if game.is_game_over():
        game_is_on = False
    screen.update()
else:
    print("end")
screen.exitonclick()
