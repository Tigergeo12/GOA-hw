from turtle import *

speed(0)

width(5)
forward(300)
left(90)
forward(200)
left(90)
forward(300)
left(90)
forward(200)
left(90)

penup()
goto(0, 68)
pendown()
begin_fill()
color("green")
forward(300)
right(90)
forward(68)
right(90)
forward(300)
right(90)
end_fill()
forward(68)

color("black")
forward(68)
right(90)
begin_fill()
color("orange")
forward(300)
left(90)
forward(64)
left(90)
forward(300)
left(90)
forward(64)
end_fill()

color("blue")
penup()
goto(130, 100)
pendown()
circle(25)



exitonclick()