import turtle
win = turtle.Screen()
win.screensize(400,400)
win.title("spiral square")
win.bgcolor("black")
t = turtle.Turtle()
t.color('deeppink')
for i in range(200):
    t.forward(10+i*4)
    t.right(90)

  


turtle.done()
