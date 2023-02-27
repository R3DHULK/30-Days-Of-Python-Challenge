from turtle import *
 
#writing speed
speed(0)
 
penup()
goto(0, -250)
pendown()
#change the bg color
color("lightskyblue")
begin_fill()
circle(250)
end_fill()
 
# Tree Trunk
penup()
goto(-15, -50)
pendown()
color("brown")
begin_fill()
for i in range(2):
    forward(30)
    right(90)
    forward(40)
    right(90)
end_fill()
 
# Set the start position and the inital tree width
y = -50
width = 240
height = 25
 
while width > 20:
    width = width - 30 # Make the tree get smaller as it goes up in height
    x = 0 - width / 2 # Set the starting x-value of each level of the tree
    color("green")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()
 
    y = y + height # Keep drawing the levels of the tree higher than the previous
 
# Star
penup()
goto(-15, 150)
pendown()
color("yellow")
begin_fill()
for i in range(5):
    forward(30)
    right(144)
end_fill()
 
# Message
penup()
goto(-130, -150)
color("red")
write("MERRY CHRISTMAS", font=("Arial", 20, "bold"))
penup()
goto(-130, -200)
color("black")
 
write("Coded By Sumalya Chatterjee", font=("Arial", 10))
 
 
hideturtle()
done()