from turtle import *
import random
import colorgram
from PIL import Image

my_image = Image.open("day_18/download.webp")
colors = colorgram.extract(my_image, 10)

rgb_colors = []
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)

turtle = Turtle()
turtle.speed("fastest")
turtle.penup()
turtle.setposition((-400, -400))

for i in range(16):
    for j in range(16):
        turtle.color(random.random(), random.random(), random.random())
        turtle.pendown()
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)
    turtle.setposition((-400, -400 + (i + 1) * 50))


screen = Screen()
screen.exitonclick()
