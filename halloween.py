# importing libraries
from turtle import *
import turtle
# initalizing a variable for turtle
t = turtle.Turtle()
# creating turtle screen
screen = turtle.Screen()
# setting up the screen size of canvas
screen.setup(900, 650)
# changing the color of background to black
screen.bgcolor('black')
# defining speed of turtle
t.speed(50)
t.hideturtle()
# deciding the color for circle
t.fillcolor("#DC5F00")
# start the filling color
t.begin_fill()
t.up()
# radius of circle
r = 180
t.goto(0, -240)
t.circle(r)
# end filling the colour
t.end_fill()
# drawing triangle for eyes
# left eye
t.up()
t.setpos(-140, -45)
t.fillcolor("gold")
t.begin_fill()
t.forward(100)  # draw base
t.left(120)
t.forward(100)  # draw second side
t.left(120)
t.forward(100)  # draw third side
t.end_fill()
# right eye
t.up()
t.setpos(90, 40)
t.fillcolor("gold")
t.begin_fill()
t.forward(100)  # draw base
t.left(120)
t.forward(100)  # draw second side
t.left(120)
t.forward(100)  # draw third side
t.end_fill()
# drawing inverted triangle for nose
t.up()
t.setpos(0, -110)
t.fillcolor("gold")
t.begin_fill()
t.forward(40)
t.right(120)
t.forward(40)
t.right(120)
t.forward(40)
t.end_fill()
# drawing triangle for tooth of pumpkin🎃
# triangle 1
t.up()
t.setpos(-60, -120)
t.fillcolor("gold")
t.begin_fill()
t.forward(50)
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
t.end_fill()
# triangle 2
t.up()
t.setpos(-60, -120)
t.fillcolor("gold")
t.begin_fill()
t.forward(50)  # draw base
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
t.end_fill()
# trinagle 3
t.up()
t.setpos(14, -163)
t.fillcolor("gold")
t.begin_fill()
t.forward(50)  # draw base
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
t.end_fill()
# trinagle 4
t.up()
t.setpos(90, -120)
t.fillcolor("gold")
t.begin_fill()
t.forward(50)  # draw base
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
t.end_fill()
# drawing green part of pumpkin
t.fillcolor("green")
t.begin_fill()
t.goto(-20, 110)
# drawing first side
t.forward(40)  # Forward turtle by 40 units
t.left(90)  # Turn turtle by 90 degree
# drawing second side
t.forward(60)  # Forward turtle by 60 units
t.left(90)  # Turn turtle by 90 degree
# drawing third side
t.forward(40)  # Forward turtle by 40 units
t.left(90)  # Turn turtle by 90 degree
# drawing fourth side
t.forward(60)  # Forward turtle by 60 units
t.left(90)  # Turn turtle by 90 degree
t.end_fill()
# writing happy halloween on canvas
t.goto(-250, -290)
t.pencolor("red")
t.write('Happy Halloween', font=("Courier", 14, "italic"))
# holding the screen to display
screen.mainloop()