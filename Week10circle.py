from turtle import Turtle
from math import pi


def drawCircle(t, x, y, radius):
    t.up()
    t.goto(x, y)
    t.forward(radius)
    t.left(90)
    t.down()

    for turn in range(120):
        distance = 2.0 * pi * radius / 120.0
        t.forward(distance)
        t.left(3)

def main():
    t = Turtle()
    drawCircle(t, 25, 75, 100)


main()
    


