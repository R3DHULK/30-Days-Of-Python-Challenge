# importing libraries
import turtle
# initalizing a variable for turtle
t = turtle.Turtle()
# creating turtle screen
screen = turtle.Screen()
# setting up the screen size of canvas
screen.setup(1200, 600)
# changing the color of background to black
screen.bgcolor('black')
t.pencolor("red")
t.penup()
t.goto(-500, -20)
# defining font size, color and type
t.write('Happy Halloween', font=("Courier", 80, "italic"))
# from here we are adding colourful circles on our canvas
# deciding the color for circle
t.fillcolor("blue")
# start the filling color
t.begin_fill()
# radius of circle
r = 10
t.goto(100, 100)
t.circle(r)
# end filling the colour
t.end_fill()

# making different circles and different positions for different colours
t.fillcolor("white")
t.begin_fill()
t.goto(-100, -100)
t.circle(r)
t.end_fill()

t.fillcolor("green")
t.begin_fill()
t.goto(-200, -200)
t.circle(r)
t.end_fill()

t.fillcolor("orange")
t.begin_fill()
t.goto(100, -100)
t.circle(r)
t.end_fill()

t.fillcolor("yellow")
t.begin_fill()
t.goto(-100, 100)
t.circle(r)
t.end_fill()

t.fillcolor("pink")
t.begin_fill()
t.goto(-250, -150)
t.circle(r)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
t.goto(-250, 150)
t.circle(r)
t.end_fill()

t.fillcolor("blue")
t.begin_fill()
t.goto(250, -150)
t.circle(r)
t.end_fill()

t.fillcolor("yellow")
t.begin_fill()
t.goto(-300, -200)
t.circle(r)
t.end_fill()

# holding the screen
screen.mainloop()
