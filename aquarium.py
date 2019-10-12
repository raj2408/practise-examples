import turtle

screen = turtle.Screen()
screen.setup(500, 500)
screen.tracer(0)
screen.addshape("sorry.gif")  # register the image with the screen as a shape
don = turtle.Turtle()
don.speed(0)
don.shape("sorry.gif")  # now set the turtle's shape to it
don.penup()
don.goto(-350, 0)
while True:
    screen.update()
    don.forward(0.01)

    screen.addshape("smiley.gif")
    don2 = turtle.Turtle()
    don2.speed(0)
    don2.shape("smiley.gif")  # now set the turtle's shape to it
    don2.penup()
    don2.goto(250, 0)
    while True:
      screen.update()
      don2.backward(0.01)