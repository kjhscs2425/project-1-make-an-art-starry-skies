
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
    draw_turtle()
    turtle.teleport(-69,180)
turtle.teleport(-69,180)
for i in range(2):
    radius=14
    turtle.color("black")
    turtle.begin_fill()
    draw_turtle()
    turtle.end_fill()
    turtle.teleport(57,180)
turtle.teleport(-69,100)
turtle.right(70)
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
turtle.teleport(30,39)
for i in range(2):
   turtle.left(180)
   draw_teeth()
   turtle.left(180)
   turtle.backward(30)
turtle.teleport(-10,300)
def draw_petal(diameter):
   turtle.circle(diameter,angle+10)
   turtle.left(40)
   turtle.circle(diameter,angle)
for i in range (11):
   angle=150
   right=21.4
   turtle.pensize(5)
   if i%2==0:
      turtle.color("black")
      turtle.begin_fill()
      draw_petal(78)
      turtle.end_fill()
      turtle.right(right)
      turtle.forward(40)
   if i%2 != 0:
      draw_petal(98)
      turtle.right(right)
      turtle.forward(40)
def draw_stem():
   turtle.pensize(8)
   turtle.teleport(10,0)
   turtle.right(107)
   turtle.forward(330)
draw_stem()
for i in range(2):
   angle=130
   turtle.pensize(4)
   turtle.teleport(10,-200)
   turtle.left(30)
   draw_petal(40)
   turtle.right(30)
   
turtle.exitonclick()