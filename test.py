import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.register_shape("carrot.gif")
t.shape("carrot.gif")
#t.resizemode("user")
#t.shapesize(0.05, 0.05, 1)

t.forward(100)

screen.mainloop()