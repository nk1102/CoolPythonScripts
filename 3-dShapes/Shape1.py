import turtle as t
t.bgcolor('black')
t.speed(0)
t.pencolor('cyan')

for i in range(0,360//5):
    t.right(5)
    t.circle(120)
t.exitonclick()