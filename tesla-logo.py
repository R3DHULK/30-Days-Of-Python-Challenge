import turtle

logo = '''
     Author :: Sumalya Chatterjee
     Github :: https://github.com/R3DHULK/
     Youtube:: https://youtube.com/@sumalya
     Website::https://r3dhulk.github.io/
'''
print('logo')
t=turtle.Turtle()

t.getscreen().bgcolor("black")
t.pencolor("white")
t.speed(4)

t.color("#E82127")
t.penup()
t.goto(-160,160)
t.pendown()

t.begin_fill()
t.left(18)
t.circle(-500,40)
t.right(90)
t.forward(17)

t.right(89.5)
t.circle(500,39)
t.right(90)
t.forward(17)
t.end_fill()

t.penup()
t.goto(-155,133)
t.pendown()

t.begin_fill()
t.right(90.5)
t.circle(-500,38)
t.right(70)
t.circle(-30,80)
t.left(90)
t.circle(-20,-70)
t.right(10)
t.circle(-300,-15)
t.right(93)
t.forward(280)
t.right(160)
t.forward(280)
t.left(80)
t.circle(300,15)
t.circle(20,70)
t.left(80)
t.circle(30,-80)
t.end_fill()

t.penup()
t.goto(-20,155)
t.pendown()
t.pencolor("black")
t.color("black")
t.begin_fill()
t.left(30)
t.forward(60)
t.left(130)
t.forward(65)
t.end_fill()

# T letter
t.pencolor("#E82127")
t.penup()
t.goto(-200,-180)
t.pendown()
t.right(66)

t.pensize(15)
t.forward(60)
t.back(30)
t.right(90)
t.forward(70)

#E Letter
t.penup()
t.goto(-115,-180)
t.pendown()
t.left(90)
t.forward(60)
t.penup()
t.goto(-115,-215)
t.pendown()
t.forward(60)
t.penup()
t.goto(-115,-250)
t.pendown()
t.forward(60)

# S letter
t.penup()
t.goto(-20,-180)
t.pendown()
t.forward(60)
t.backward(60)
t.right(90)
t.forward(34)
t.left(90)
t.forward(60)
t.right(90)
t.forward(34)
t.right(90)
t.forward(60)

# L letter
t.penup()
t.goto(70,-180)
t.pendown()
t.left(90)
t.forward(70)
t.left(90)
t.forward(60)

# A letter
t.penup()
t.goto(155,-180)
t.pendown()
t.forward(60)

t.penup()
t.goto(155,-250)
t.pendown()
t.left(90)
t.forward(32.5)
t.right(90)
t.forward(60)
t.right(90)
t.forward(32.5)

t.hideturtle()
turtle.done()