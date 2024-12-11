#start

#Definition alt+shift+A multi line comments
""" 1. be able to detect inputs.
2. require multiple inputs to pop the balloon.
3. Utilize variables, conditions and functions. """

#import turtle
from turtle import *

diameter = 40
pop_diameter = 100

def draw_balloon ():
    color("red")
    dot(diameter)

def inflate_balloon ():
    global diameter
    diameter = diameter + 10
    draw_balloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write ("POP!")

draw_balloon()

#Screen().onkey() screen is required for onkey and listen using trinket.
onkey(inflate_balloon, "Up")
listen()

done()