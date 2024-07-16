from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")
player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

game_is_on = True

screen.listen()
screen.onkey(player.up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.level_up()
        car_manager.level_up()

screen.exitonclick()
