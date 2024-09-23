

import turtle
numberofsides = 100
turtle.speed(10)
height=2000
width=2000
turtle.screensize(width,height)
def draw_turtle():
    import turtle
    turtle.speed(140)
    turtle.pensize(4)
    turtle.circle(radius)
    turtle.right(360/numberofsides)
for i in range (1):
    radius=150
    draw_turtle()
turtle.teleport(59,180)
for i in range(2):
    radius=20
    turtle.color("black")
    turtle.begin_fill()
    draw_turtle()
    turtle.end_fill()
    turtle.teleport(-69,180)
turtle.right(80)
turtle.teleport(-69,100)
for i in range(1):
 turtle.circle(70,180)
turtle.left(90)
turtle.forward(140)
turtle.left(180)
def draw_teeth():
    for i in range(3):
     turtle.forward(30)
     turtle.right(360/3)
for i in range(5):
    draw_teeth()
    turtle.forward(140/5)
turtle.teleport(30,35)
for i in range(2):
   turtle.left(180)
   draw_teeth()
   turtle.left(180)
   turtle.backward(30)
turtle.teleport(-10,300)
def draw_petal():
   turtle.circle(diameter,angle+10)
   turtle.left(40)
   turtle.circle(diameter,angle)
for i in range (12):
   diameter=100
   angle=150
   if i%2==0:
      turtle.color("black")
      turtle.begin_fill()
      draw_petal()
      turtle.end_fill()
      turtle.right(19.75)
      turtle.forward(30)
   if i%2 != 0:
      draw_petal()
      turtle.right(19.75)
      turtle.forward(30)
turtle.exitonclick()