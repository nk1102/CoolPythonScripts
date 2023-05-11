import turtle as t
import colorsys

t.bgcolor('black')
t.setpos(-90,80)
t.tracer(100)

# cool shapes updated here

t.pensize(1)
hue = 0
t.hideturtle()

for i in range(600):
    color = colorsys.hsv_to_rgb(hue,0.6,0.8)
    t.pencolor(color)

# updated the for in range method
    t.fd(200)
    t.rt(91)
    t.circle(59)
    hue  += 0.009

t.exitonclick()