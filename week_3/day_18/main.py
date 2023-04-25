from turtle import *
import random

turtle = Turtle()

turtle.color("#14b8a6")
turtle.shape("turtle")


# Challenge 1 -> Draw a Square
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)


turtle.right(90)

# Challenge 2 -> Draw a Dashed Line
for i in range(10):
    if i % 2 == 0:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.forward(10)


turtle.right(90)
turtle.pendown()

# Challenge 3 -> Drawing Different Shapes
for number_of_sides in range(3, 11):
    angle = 360 / number_of_sides
    turtle.color(random.random(), random.random(), random.random())

    for side in range(number_of_sides):
        turtle.forward(100)
        turtle.left(angle)

turtle.penup()
turtle.setpos((-400, 400))
turtle.pendown()

# Challenge 4 -> Generate a Radom Walk
directions = [0, 90, 180, 270]

for i in range(150):
    turtle.color(random.random(), random.random(), random.random())
    turtle.pensize(15)
    turtle.speed("fastest")
    turtle.forward(40)
    turtle.setheading(random.choice(directions))
    # turtle.setheading(int(random.random() * 360))


# Challenge 5 -> Draw a Spirograph
turtle.penup()
turtle.setpos((0, 0))
turtle.pensize(2)
turtle.pendown()

for i in range(72):
    turtle.color(random.random(), random.random(), random.random())
    turtle.circle(100)
    turtle.setheading(turtle.heading() + 5)


screen = Screen()
screen.exitonclick()
