import turtle

win = turtle.Screen()
win.screensize(400,400)
win.title("polygon")
win.bgcolor('lime')

t = turtle.Turtle()
t.color("red")
n = 6
for i in range(n):
    t.forward(100)
    t.right(360/n)







turtle.done()