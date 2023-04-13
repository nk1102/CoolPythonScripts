from turtle import *
import colorsys

speed(0)
hideturtle()
bgcolor("black")
tracer(5)
width(2)
h = 0.001

for i in range(90):
    color(colorsys.hsv_to_rgb(h,1,1))
    forward(100)

    forward(100)
    right(320)
    circle(50)
    left(240)
    forward(100)
    left(-50)
    left(60)
    forward(100)
    h += 0.02
    color(colorsys.hsv_to_rgb(h,1,1))
    forward(100)
    right(60)
    forward(100)
    left(120)
    circle(-50)
    right(210)
    forward(50)
    right(60)
    forward(100)
    left(2)
    h += 0.02
done()