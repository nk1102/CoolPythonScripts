import turtle
import colorsys
t=turtle.Turtle()
turtle.Screen().bgcolor("black")
t.pensize(2)
t.speed(5)
n = 36
h=0

for i in range(21):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.pencolor(c)
    t.circle(105,103)
    t.backward(200)
    t.left(60)
    t.circle(70,68)
    t.right(87)
    t.forward(150)
    t.left(90)
turtle.done()