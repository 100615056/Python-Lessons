# Drawing shapes with the turtle library

import turtle

# Create window and turtle
w = turtle.getscreen()
t = turtle.Turtle()


# Setting up screen
def screen(color, title):
    w.bgcolor(color)
    w.title(title)


# Setting up the turtle
def turtle(shape):
    t.shape(shape)


# Setting up the pen
def pen(size, pencolor, fillcolor, speed):
    t.pensize(size)
    t.pencolor(pencolor)
    t.fillcolor(fillcolor)
    t.speed(speed)

# Display shape menu 
def shape_input():
    list = ['square', 'zigzag', 'spiral', 'triangle', 'polygon', 'custom']
    for i, item in enumerate(list):
        print(i, item)
    shape = int(input('Please enter a number: '))
    print(shape)

# Initial setup for drawing shapes
def start(x, y):
    t.setposition(x, y)
    t.pd()

# Create functions for common turtle drawing motions
def fwdR(distance, angle):
    t.fd(distance)
    t.right(angle)


def fwdL(distance, angle):
    t.fd(distance)
    t.left(angle)

# Draw square shape
def square(x, y, size, angle):
    start(x, y)
    t.right(angle)
    t.begin_fill()
    for i in range(4): 
        fwdR(size, angle)
    t.left(angle)
    t.end_fill()

# Draw zigzag shape
def zigzag(x, y, size, angle):
    start(x, y)
    t.begin_fill()
    for i in range(4):
        fwdR(size, angle)
        fwdL(size, angle)
    fwdR(size, angle)
    t.fd(size)
    t.end_fill()


def spiral(x, y, size, angle):
    start(x, y)
    length = 2 * size
    for i in range(14):  # 0-13
        fwdR(length, angle)
        length += 10


def triangle(x, y, side, angle):
    start(x, y)
    t.begin_fill()
    for i in range(2):
        fwdL(side, angle)
    t.fd(side)
    t.end_fill()


def polygon(x, y, sides, length, angle):
    start(x, y)
    t.begin_fill()
    for i in range(sides):
        fwdR(length, angle)
    t.end_fill()


def main():
    # Screen
    screen_color = "white"
    text = "Turtle Drawing"
    # Turtle
    shape = "turtle"
    # Pen
    pen_color = "blue"
    fill_color = "orange"
    # Setting Up
    screen(screen_color, text)
    turtle(shape)
    pen(5, pen_color, fill_color, 5)
    # Turtle Drawing
    # Square
    x = 0
    y = 0
    square_distance = 100
    square_angle = 90
    # square(x, y, square_distance, square_angle)
    # ZigZag
    zigzag_distance = 25
    zigzag_angle = 45
    # zigzag(x, y, zigzag_distance, zigzag_angle)
    # Spiral
    spiral_distance = 10
    # spiral(x, y, spiral_distance, square_angle)
    # Triangle
    side = 100
    angle = 120
    # triangle(x, y, side, angle)
    # Polygon
    sides = 15
    length = 50
    polygon_angle = 360 / sides
    # polygon(x, y, sides, length, polygon_angle)
    shape_input()


main()

