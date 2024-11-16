import turtle
win = turtle.Screen()
win.screensize(400,400)
win.title("spiral")
win.bgcolor('black')

t = turtle.Turtle()
t.color("gold")

for i in range(200):
    t.forward(i*3)
    t.left(90)
    
turtle.done()