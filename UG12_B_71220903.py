import turtle
t = turtle.Turtle()
t.speed(2)
t.pensize(10)
s=turtle.Screen()
s.bgcolor('black')

t.color('blue')
a =100
for i in range (a):
    t.left(115)
    t.forward(158)
    t.backward(150)
    t.right(60)
    t.forward(158)
    t.backward(150)
    t.right(145)
    t.forward(158)
    t.penup()
    t.backward(150)
    t.left(98)
    t.pendown()
    t.hideturtle()
    turtle.done()
