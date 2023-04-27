import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
i = 0
while game_is_on:
    if i % 6 == 0:
        car_manager.generate_car()

    car_manager.move_cars()

    # detect if turtle collides with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False

    # detect if turtle finishes the game
    if player.ycor() > 280:
        player.restart_position()
        car_manager.increase_level()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()

    time.sleep(0.1)
    i += 1
    screen.update()


screen.exitonclick()
