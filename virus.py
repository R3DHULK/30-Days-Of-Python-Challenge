#Import Turtle
import turtle

tt=turtle.Turtle()
turtle.bgcolor("yellow")#Screen background color set to gray
tt.pencolor("black")#Pencolor set to black

tt.speed(0)
tt.penup()
tt.goto(0,200)#position of the turtle 
tt.pendown()

#Intialization of variables 
forDis=0 
dR=0

while(True):
    tt.forward(forDis)
    tt.right(dR)
    forDis+=3 # forDis increased by 3 on every iteration
    dR+=1# right angle distance increased by 1 on every iteration 
    #If the distance for right angle becomes 210 the loop breaks
    if dR==210:
        break
	#Hide the turtle on completion of loop
    tt.hideturtle()

#Completion of Turtle execution
turtle.done()