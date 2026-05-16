import turtle

turtle.Screen().bgcolor("Magenta")
turtle.Screen().setup(500,700)
polygon = turtle.Turtle()

side_length = 0

while True :
    for i in range(4):
       
     polygon.forward(side_length+1)
     polygon.left(90)
     side_length = side_length-5
     

    side_length = side_length+1
turtle.done()
