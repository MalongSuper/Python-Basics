# Drawing Python logo
import turtle

# Create turtle cursor to draw
turtle_cursor = turtle.Turtle()

# Create Canvas to draw Python logo
screen = turtle.Screen()


def goto_second_position():
    turtle_cursor.penup()
    turtle_cursor.forward(20)
    turtle_cursor.right(90)
    turtle_cursor.forward(10)
    turtle_cursor.right(90)
    turtle_cursor.pendown()


def draw_upper_dot():
    turtle_cursor.penup()
    turtle_cursor.right(90)
    turtle_cursor.forward(160)
    turtle_cursor.left(90)
    turtle_cursor.forward(70)
    turtle_cursor.pencolor("white")
    turtle_cursor.dot(35)


def draw_lower_dot():
    turtle_cursor.left(90)
    turtle_cursor.penup()
    turtle_cursor.forward(310)
    turtle_cursor.left(90)
    turtle_cursor.forward(120)
    turtle_cursor.pendown()

    turtle_cursor.dot(35)


def draw_side_curve():
    for i in range(90):
        turtle_cursor.left(1)
        turtle_cursor.forward(1)


def draw_first_left_curve():
    draw_side_curve()
    turtle_cursor.forward(80)
    draw_side_curve()


def draw_second_left_curve():
    draw_side_curve()
    turtle_cursor.forward(90)
    draw_side_curve()


def draw_right_curve():
    for i in range(90):
        turtle_cursor.right(1)
        turtle_cursor.forward(1)


def half():
    turtle_cursor.forward(50)
    draw_side_curve()
    turtle_cursor.forward(90)
    draw_first_left_curve()
    turtle_cursor.forward(40)
    turtle_cursor.left(90)
    turtle_cursor.forward(80)
    turtle_cursor.right(90)
    turtle_cursor.forward(10)
    turtle_cursor.right(90)
    turtle_cursor.forward(120)
    draw_second_left_curve()
    turtle_cursor.forward(30)
    turtle_cursor.left(90)
    turtle_cursor.forward(50)
    draw_right_curve()
    turtle_cursor.forward(40)
    turtle_cursor.end_fill()


# Set configuration for the cursor
turtle_cursor.pensize(2)
turtle_cursor.speed(2)
turtle_cursor.pensize(2)
turtle_cursor.pencolor("black")

# Changed background color of canvas
screen.bgcolor("white")

# Fill color for the upper part of the logo
turtle_cursor.fillcolor("#306998")
turtle_cursor.begin_fill()

half()
turtle_cursor.end_fill()

goto_second_position()


# Fill color for the lower part of the logo
turtle_cursor.fillcolor("#FFD43B")
turtle_cursor.begin_fill()

half()
turtle_cursor.end_fill()

# Drawing upper and lower dot of logo
draw_upper_dot()
draw_lower_dot()

# Finalize
turtle_cursor.hideturtle()
turtle.done()
