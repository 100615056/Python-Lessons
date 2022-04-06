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

# Shape Menu
def print_menu():
    shapes = ['square', 'zigzag', 'spiral', 'triangle', 'polygon', 'clear', 'exit']
    print('----------')
    for i, item in enumerate(shapes):
        print(i+1, item)
    print('----------')
    
    
# Initial setup for drawing shapes
def setup():
    while True:
        cx = input('X-Coordinate: ')
        if not cx.isnumeric():
            print('Enter valid x-coordinate')
            continue
        cy = input('Y-Coordinate: ')
        if not cy.isnumeric():
            print('Enter valid y-coordinate')
            continue
        else:
            x = int(cx)
            y = int(cy)
            t.penup()
            t.setposition(x, y)
            t.setheading(0)
            t.pd()
            break

            
# Create functions for common turtle drawing motions
def fwdR(distance, angle):
    t.fd(distance)
    t.right(angle)


def fwdL(distance, angle):
    t.fd(distance)
    t.left(angle)

    
def square(size, angle):
    setup()
    t.right(angle)
    t.begin_fill()
    for i in range(4): 
        fwdR(size, angle)
    t.end_fill()

    
def zigzag(size, angle):
    setup()
    t.begin_fill()
    for i in range(4):
        fwdR(size, angle)
        fwdL(size, angle)
    fwdR(size, angle)
    t.fd(size)
    t.end_fill()


def spiral(size, angle):
    setup()
    length = 2 * size
    for i in range(14): 
        fwdR(length, angle)
        length += 10


def triangle(side, angle):
    setup()
    t.begin_fill()
    for i in range(2):
        fwdL(side, angle)
    t.fd(side)
    t.end_fill()

# User-defined polygon
def polygon_input():
    while True:
        size = input('Enter side number (3-15): ')
        if size.isnumeric():
            side = int(size)
            if side > 3 and side < 15:
                return side
            else:
                print('Invalid side number')
     
    
def polygon(sides, length, angle):
    setup()
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
    pen_color = "black"
    fill_color = "green"
    # Setting Up
    screen(screen_color, text)
    turtle(shape)
    pen(5, pen_color, fill_color, 5)
    # Turtle Drawing
    # Square
    square_distance = 100
    angle_90 = 90
    # ZigZag
    zigzag_distance = 25
    zigzag_angle = 45
    # Spiral
    spiral_distance = 10
    # Triangle
    side = 100
    angle = 120
    # Polygon
    length = 30
    # Draw Selection
    while True:
        print_menu()
        choice = int(input("Select menu item: "))
        if choice == 1:
            square(square_distance,angle_90)
        if choice == 2:
            zigzag(zigzag_distance, zigzag_angle)
        if choice == 3:
            spiral(spiral_distance, angle_90)
        if choice == 4:
            triangle(side, angle)
        if choice == 5:
            sides = polygon_input()
            polygon_angle = 360 / sides
            polygon(sides, length, polygon_angle)
        if choice == 6:
            t.clear()
        if choice == 7:
            break

            
main()
