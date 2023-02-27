# Importing turtle library to draw "I Love You"
import turtle

# Creating our turtle cursor to draw
my_turtle_cursor = turtle.Turtle()

# Creating a separate Canvas to draw "I Love You"
my_turtle_screen = turtle.Screen()


# Creating a pause function to pause the cursor
def pause():
    my_turtle_cursor.speed(2)
    for i in range(100):
        my_turtle_cursor.left(90)


# Function to write "I" inside heart
def write_I_inside_heart():

    my_turtle_cursor.penup()

    # Co-ordinates where we have to write "I"
    my_turtle_cursor.goto(-230, 15)

    # Setting the text color of our text
    my_turtle_cursor.pencolor("#FFFFFF")

    # Adding the text and changing the font of our text
    my_turtle_cursor.write("I", font=("Helevetica", 54, "bold"))



# Function to write "Love" inside heart
def write_Love_inside_heart():

    my_turtle_cursor.penup()

    # Co-ordinates where we have to write "Love"
    my_turtle_cursor.goto(-160, 15)

    # Setting the text color of our text
    my_turtle_cursor.pencolor("#FFFFFF")

    # Adding the text and changing the font of our text
    my_turtle_cursor.write("Love", font=("Helevetica", 54, "bold"))


# Function to write "You" inside heart
def write_you_inside_heart():

    my_turtle_cursor.penup()

    # Co-ordinates where we have to write "You"
    my_turtle_cursor.goto(80, 15)

    # Setting the text color of our text
    my_turtle_cursor.pencolor("#FFFFFF")

    # Adding the text and changing the font of our text
    my_turtle_cursor.write("You", font=("Helevetica", 54, "bold"))


# Method to draw a heart
def draw_complete_heart():
    # Set the fill color to #FF0000
    my_turtle_cursor.fillcolor("#FF0000")

    # Start filling the color
    my_turtle_cursor.begin_fill()

    # Draw the left line
    my_turtle_cursor.left(140)
    my_turtle_cursor.forward(294)

    # Calling the function to draw left curve of our heart
    draw_left_curve_of_heart()

    # Draw the left line
    my_turtle_cursor.right(190)

    # Calling the function to draw right curve of our heart
    draw_right_curve_of_heart()

    # Draw the right line
    my_turtle_cursor.forward(294)

    # Ending the filling of the color
    my_turtle_cursor.end_fill()


# Defining a method to draw left curve
def draw_left_curve_of_heart():

    my_turtle_cursor.speed(50)
    # For Loop for creating left curves
    for i in range(450):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.forward(1.2)


# Defining a method to draw right curve
def draw_right_curve_of_heart():

    my_turtle_cursor.speed(50)
    # For Loop for creating right curves
    for i in range(450):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.forward(1.2)


# Changing start position of our turtle cursor
my_turtle_cursor.penup()
my_turtle_cursor.goto(0, -200)
my_turtle_cursor.pendown()

# Setting the speed of our cursor
my_turtle_cursor.speed(50)

# Calling a Function to Draw a complete Heart Background
draw_complete_heart()

# Calling a Function to write "I" Inside our hearth Background
write_I_inside_heart()

# Calling a Function to write "Love" Inside our hearth Background
write_Love_inside_heart()

# Calling a Function to write "You" Inside our hearth Background
write_you_inside_heart()

turtle.done()