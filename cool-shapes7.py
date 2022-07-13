import turtle
import colorsys
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.pensize(2)
t.speed(0)
n = 36
h = 0
for i in range(60):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.pencolor(c)
    for j in range(4):
        t.forward(i)
        t.right(10*5)
        t.left(10)
        t.forward(i)
    t.right(120)
turtle.done()
