import turtle as t
import colorsys

t.bgcolor('black')
t.setpos(-90,80)
t.tracer(100)

# cool shapes updated here

t.pensize(12)
hue = 0
t.hideturtle()

for i in range(400):
    color = colorsys.hsv_to_rgb(hue,0.6,0.8)
    t.pencolor(color)

# updated the for in range method
