#import the time and turtle module
import turtle
import time

# create a screen
scr = turtle.getscreen()
scr.title("Flag of America")
scr.bgcolor("white")

#Set the turtle object and speed of the turtle

t = turtle.Turtle()
t.speed(20)
t.penup()

# flag height and width
flag_ht = 250
flag_wth = 475

# starting points of the flag
x1 = -250
y1 = 120

# red and white stripes (total 13 stripes in flag)
stripe_ht = flag_ht/13
stripe_wdt = flag_wth
#star size
star_size = 12


def draw_rectangle(x, y, height, width, color):
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.end_fill()
    t.penup()

def star_shape(x,y,color,length) :
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.color(color)
    for turn in range(0,5) :
        t.forward(length)
        t.right(144)
        t.forward(length)
        t.right(144)
    t.end_fill()
    t.penup()


# function to create stripes of flag
def draw_stripes():
    x = x1
    y = y1
    # draw 6 red and 7 white strips
    for stripe in range(0,6):
        for color in ["red", "white"]:
            draw_rectangle(x, y, stripe_ht, stripe_wdt, color)
            # decrease value of y by stripe_height
            y = y - stripe_ht

    # create last red stripe
    draw_rectangle(x, y, stripe_ht, stripe_wdt, 'red')
    y = y - stripe_ht


# this function create navy color square
def draw_square():
    square_ht = (7/13) * flag_ht
    square_wdt = (0.76) * flag_ht
    draw_rectangle(x1, y1, square_ht, square_wdt, 'navy')

#defining a function for drawing a 6 row star
def stars1():
    dist_of_stars = 30
    dist_bet_lines = stripe_ht + 6
    y = 112
    # create 5 rows of stars
    for row in range(0,5) :
        x = -234
        # create 6 stars in each row
        for star in range (0,6) :
            star_shape(x, y, 'white', star_size)
            x = x + dist_of_stars
        y = y - dist_bet_lines


def stars_five():
    dist_of_stars = 30
    dist_bet_lines = stripe_ht + 6
    y = 100
    # create 4 rows of stars
    for row in range(0,4) :
        x = -217
        # create 5 stars in each row
        for star in range (0,5) :
            star_shape(x, y, 'white', star_size)
            x = x + dist_of_stars
        y = y - dist_bet_lines
        
#Call all the functions
# start after 5 seconds.
time.sleep(5)
# draw 13 stripes
draw_stripes()
# draw squares 
draw_square()
# draw 30 stars, 6 * 5
stars1()
# draw 20 stars, 5 * 4
stars_five()
# hides the turtle
t.hideturtle()
scr.mainloop()