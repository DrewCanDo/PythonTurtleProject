#Solar system algorithem using python turtle
#60px Radius ORG - 80px space - 20px R GREY- 80px space - 40px R RED- 90px space - 30px R GREEN
#bg is black
from turtle import *

#screen setkup for live coding
Screen().setup(900,750)

#set the speed of the animation
speed(0)

#background color
bgcolor('black')

#set up the white circle
color('white')
left(90)
penup()
forward(100)
pendown()
circle(120)

left(90)
penup()
forward(60)
right(90)
pendown()

#set up the sun
color('orange')
begin_fill()
circle(60)
end_fill()
penup()
right(90)
forward(60)
pendown()


#set up teh grey planet
color('grey')
begin_fill()
circle(20)
end_fill()
penup()
forward(80)
pendown()

#white circle
color('white')
left(90)
circle(190)
right(90)

#red planet
color('red')
begin_fill()
circle(40)
end_fill()
penup()
forward(90)
pendown()

#whtie circle
color('white')
left(90)
circle(280)
right(90)

#greem planet set up
color('green')
begin_fill()
circle(30)
end_fill()

#stop the screen from closing.
done()