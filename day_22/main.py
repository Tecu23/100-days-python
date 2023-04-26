from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("#000000")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

    # detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
        ball.distance(left_paddle) < 50 and ball.xcor() < -320
    ):
        ball.bounce_x()
        ball.increase_speed()

    # detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_player_scores()
        scoreboard.update_scoreboard()
        ball.reset_speed()

    # detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_player_scores()
        scoreboard.update_scoreboard()
        ball.reset_speed()

screen.exitonclick()
