import turtle
colors = ['yellow' , 'green' , 'red' , 'white', 'cyan', 'blue']
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('Black')
t.speed(30)

for i in range(120):
    t.color(colors[i%6])
    t.fd(i*8)
    t.left(200)
    t.width(0.9)

# Star shapes
#