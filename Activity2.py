import turtle

turtle.Screen().bgcolor("Aqua")
turtle.Screen().setup(700,700)
polygon = turtle.Turtle()

num_sides = 3
side_length = 80
angle = 360/num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.left(angle)

polygon.penup()
polygon.goto(0,50)
polygon.pendown()

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)


turtle.done()