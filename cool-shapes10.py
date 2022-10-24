import turtle
import colorsys
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.pensize(6)
t.speed(-100)
n = 100
h=0
for i in range(90):
    c = colorsys.hsv_to_rgb(h,1,0.6)
    h+=1/n
    t.color(c)
    t.left(216)
    t.forward(i*2)
    t.right(40)
    t.backward(i*3)
    t.circle(60,90)
turtle.done()
