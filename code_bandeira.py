import turtle
from turtle import Turtle

t = Turtle()

t.speed(5)
t.goto(-270, -180)
t.begin_fill()
t.pencolor('green')
t.fillcolor('green')
for i in range(2):
    t.forward(550)
    t.left(90)
    t.forward(276)
    t.left(90)

t.end_fill()

t.left(90)
t.forward(138)
t.right(90)
t.forward(50)
t.begin_fill()
t.pencolor('yellow')
t.fillcolor('yellow')
t.left(25)

for i in range(2):
    t.forward(250)
    t.right(50)
    t.forward(250)
    t.right(130)

t.end_fill()
t.right(25)
t.forward(175)
t.right(90)
t.begin_fill()
t.pencolor('blue')
t.fillcolor('blue')
t.circle(50)
t.end_fill()

input('asas')
