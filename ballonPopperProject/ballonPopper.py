#start

#Definition alt+shift+A multi line comments
""" 1. be able to detect inputs.
2. require multiple inputs to pop the balloon.
3. Utilize variables, conditions and functions. """

#import turtle
from turtle import *

hideturtle()

diameter = 40
pop_diameter = 100
balloon_color = "red"

def draw_balloon ():
    color(balloon_color)
    dot(diameter)

def inflate_balloon ():
    global diameter
    global balloon_color
    diameter = diameter + 10
    draw_balloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write ("POP!")
        
        if balloon_color == "red":
            balloon_color = "blue"
        elif balloon_color == "blue":
            balloon_color = "green"
        elif balloon_color == "green":
            balloon_color = "red"
    


def deflate_balloon ():
    global diameter

    if diameter > 40:
        diameter -= 10
        clear()
        draw_balloon()
        

draw_balloon()

#Screen().onkey() screen is required for onkey and listen using trinket.
Screen().onkey(inflate_balloon, "Up")
Screen().onkey(deflate_balloon, "Down")

listen()

done()