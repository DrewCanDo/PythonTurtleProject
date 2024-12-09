from turtle import *

""" def move_and_turn (distance, angle):
    forward(distance)
    right(angle)
    # return 100 //this to the left will return 100 and can be stored using an assignment operator

#can have lines of code that use the function before it is made
move_and_turn(100, 45)
move_and_turn(50, 90) """

def draw_square(distance, x, y, color_selector = 'red'):
    penup()
    goto(x, y)
    pendown()

    color(color_selector)
    
    begin_fill()
    forward(distance)
    right(90)
    forward(distance)
    right(90)
    forward(distance)
    right(90)
    forward(distance)
    end_fill()

draw_square(100, 0, 0, 'blue')
draw_square(100, 40, 40)

done()