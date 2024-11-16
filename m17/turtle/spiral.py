import turtle
from turtle import *

win = turtle.Screen()
win.screensize(700,700)
win.bgcolor('black')
win.title('star')
colors = ['purple','silver','pink','olive','cyan','tomato']
t = turtle.Turtle()
t.speed('fastest')
while True:
    for i in range(200):
        t.color(colors[i%len(colors)])
        t.width(i/100 + 7)
        t.forward(i)
        t.right(59)
    t.left(239)
    for i in range(201,0,-1):
        t.color(colors[i%len(colors)])
        t.width(i/100 + 7)
        t.forward(i)
        t.left(59)
turtle.done()
    