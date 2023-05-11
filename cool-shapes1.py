
# cool turtle like shape
# created by Nikunj
# Python
from turtle import *
bgcolor('white')
speed(0)
hideturtle()
for i in range(200):
    color('black')
    circle(i)
    color('red')
    circle(i*0.8)
    right(3)
    forward(3)
done()
