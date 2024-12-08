#Solar system algorithem using python turtle
#60px Radius ORG - 80px space - 20px R GREY- 80px space - 40px R RED- 90px space - 30px R GREEN
#bg is black
from turtle import *

speed(0)

bgcolor('black')

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

color('orange')
begin_fill()
circle(60)
end_fill()
penup()
right(90)
forward(60)
pendown()



color('grey')
begin_fill()
circle(20)
end_fill()
penup()
forward(80)
pendown()

color('white')
left(90)
circle(190)
right(90)


color('red')
begin_fill()
circle(40)
end_fill()
penup()
forward(90)
pendown()

color('white')
left(90)
circle(280)
right(90)

color('green')
begin_fill()
circle(30)
end_fill()

done()