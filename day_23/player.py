from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.restart_position()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart_position(self):
        self.goto(STARTING_POSITION)
