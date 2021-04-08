import turtle
turtle.speed(1)
turtle.color('aqua', 'yellow')
def triangle(side_length):
    angle=120

    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)

triangle(50)
turtle.forward(50)
triangle(75)





