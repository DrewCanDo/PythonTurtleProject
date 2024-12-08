from turtle import *

"""
circle(50)
forward(100)
circle(50)
circle(30)
circle(15)
"""

# color('red')
""" color('#ffd000') #gold color
forward(100)
color('#00ff48') #green color
right(90)
forward(100) """

# challenge color circles
""" color('green')
circle(100)
color('red')
circle(50)
color('purple')
circle(25) """

""" color('red')
begin_fill()
circle(50)
end_fill() """

# challenge 
""" As a bit of a challenge, draw and fill in an equilateral triangle.

An equilateral triangle, is a triangle where all sides are of equal length,
thus all of the angles must be the same too. For this challenge, make each
side of the triangle 100 pixels. """

# color('blue')
# begin_fill()
# forward(100)
# left(120)
# forward(100)
# left(120)
# forward(100)
# left(120)
# end_fill()

# how to change background color
bgcolor('yellow')

#how to move and not draw a line
""" circle(50)
penup()
forward(100)
pendown()
circle(50) """

#draw a house


color('lightblue')
begin_fill()
#walls
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()
forward(100)
left(90)
forward(100)



color('brown')
begin_fill()
#roof
left(30)
forward(100)
left(120)
forward(100)
end_fill()

penup()
left(30)
forward(40)
left(90)
forward(50)
pendown()

color('white')
begin_fill()
circle(10)
end_fill()

done() 