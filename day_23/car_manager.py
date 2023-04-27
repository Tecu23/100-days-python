from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.level = 0
        self.cars = []

    def generate_car(self):
        new_y = random.randint(-250, 250)

        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(280, new_y)
        new_car.setheading(180)

        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)
            else:
                car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * self.level)

    def increase_level(self):
        self.level += 1
