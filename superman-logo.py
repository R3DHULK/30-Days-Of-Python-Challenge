import turtle #import the required package to draw the logo

t=turtle.Turtle() #set the variable ‘t’ to the function turtle.Turtle() to shorten the code throughout
turtle.Screen().bgcolor('navy') #set the color of the screen to navy to match Superman’s costume

def curve(value): #create a function to generate curves in turtle
    for i in range(value): #for loop to repeat the inputted value number of times 
        t.right(1) #step by step curve
        t.forward(1)

t.penup() #pen is in the up position so it will not draw
t.setposition(0,43) #move the pen to these x and y coordinates
t.pendown() #pen is in the down position so it will draw
t.begin_fill() #start filling in the shape
t.pencolor('black') #change the pen color to black
t.fillcolor('maroon') #change the shape fill color to maroon to match the Superman logo
t.pensize(3) #use a pen size of 3 to create a black border
t.forward(81.5) #the pen will move forward this number to start the shield of the logo
t.right(49.4) #rotate the pen right 49.4 degrees
t.forward(58) #move the pen forward by 58 
t.right(81.42) #rotate right by 81.42 degrees
t.forward(182) #move the pen forward by 182
t.right(98.36) #rotate the pen right by 98.36 degrees
t.forward(182) #move the pen forward by 182 
t.right(81.42) #rotate the pen by 81.42 degrees to the right
t.forward(58) #move the pen forward 58 
t.right(49.4) #rotate the pen to the right by 49.4
t.forward(81.5) #move the pen forward by 81.5 to meet the start at the top of the shield
t.end_fill() #complete the fill of the shield so the shape is closed off
t.penup() #pen will not draw 

t.setposition(38,32) #now to create the yellow parts of the Superman logo
t.pendown() #the pen is now poised to draw
t.begin_fill() #start a new shape 
t.fillcolor('gold') #change the fill color to gold to match the Superman logo
t.forward(13) #move the pen forward by 13
t.right(120) #rotate the pen right by 120 degrees
t.forward(13) #move the pen forward by 13
t.right(120) #rotate the pen right by 120 degrees
t.forward(13) #move the pen forward by 13
t.end_fill() #the small triangle on the right is now complete
t.penup() #stop the pen from drawing

t.setposition(81.5,25) #now to create the larger yellow part of the Superman logo, change the position of the pen
t.pendown() #the pen will now draw again
t.begin_fill() #the fill is still the same color set before
t.right(210) #rotate the pen right by 210 degrees
t.forward(25) #move the pen forward by 25
t.right(90) #rotate the pen right by 90 degrees
t.forward(38) #move the pen forward by 38
t.right(45) #rotate the pen right by 45 degrees
t.circle(82,90) #this function is used to draw a circle in turtle, the first integer is the radius and the second is the number of degrees of the circle drawn
t.left(90) #rotate the pen left by 90 degrees
t.circle(82,60) #create a circle of radius 82 and only complete 60 degrees of the circle 
curve(61) #call the curve function that was previously defined, pass an integer value equal to the length of the curve desired 
t.left(90) #rotate the pen left by 90 degrees
t.forward(57) #move the pen forward by 57
t.left(90) #rotate the pen left by 90 degrees
t.forward(32) #move the pen forward by 32
t.end_fill() #fill in the larger yellow part of the logo
t.penup() #stop drawing 
t.home() #reset the pen location to the origin so the orientation is also reset

t.setposition(-69,-38) #finish the major parts of the S superimposition on the shield
t.pendown()
t.begin_fill()
curve(20)
t.forward(33)
t.left(10)
t.circle(82,20)
curve(30)
t.forward(10)
t.right(110)
curve(40)
t.right(10)
t.circle(50,10)
curve(45)
t.right(5)
t.forward(45)
t.end_fill()
t.penup()
t.home()

t.setposition(20,-100)
t.pendown()
t.begin_fill()
t.right(135)
t.forward(27)
t.right(90)
t.forward(27)
t.right(135)
t.forward(38.18)
t.end_fill()
t.penup()
t.home()

t.setposition(-57,32)
t.pendown()
t.begin_fill()
t.right(180)
t.forward(18)
t.left(45)
t.forward(44)
t.left(80)
t.forward(15)
t.left(130)
curve(40)
t.forward(20)
t.end_fill()

t.hideturtle() #use this command to hide the turtle so it is not visible in the final image
turtle.exitonclick() #this command will leave the window 