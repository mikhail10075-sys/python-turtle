import turtle 
turtle.Screen().bgcolor("Blue")
turtle.Screen().setup(700,400)
polygon = turtle.Turtle()


num_sides = 6
side_length = 90
angle = 360/num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()
