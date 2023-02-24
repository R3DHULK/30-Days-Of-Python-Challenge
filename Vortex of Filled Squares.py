import turtle
import random

turtle.speed(0)
turtle.setup(1000, 700)
turtle.title('Vortex of Filled Squares')
turtle.bgcolor('black')
turtle.hideturtle()

def draw_square(x,y,size,tilt_angle,c):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.seth(tilt_angle)
    turtle.fillcolor(c)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(size)
        turtle.left(90)
    turtle.end_fill()
angle = 0
size = 240
while size > 0:
    draw_square(0,0,size,angle,(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
    size -= 0.1 
    angle +=3
turtle.done()