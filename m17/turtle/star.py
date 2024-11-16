# star program using turtle
import turtle
from turtle import *

win = turtle.Screen()
win.screensize(400,400)
win.bgcolor('black')
win.title('star')

t = turtle.Turtle()
t.color('silver')

for i in range(3):
    t.forward(100)
    t.right(120)

t.right(90)
t.penup()

t.forward(60)
t.left(90)
t.pendown()
for i in range(3):
    t.forward(100)
    t.left(120)
    
turtle.done()


turtle.done()

