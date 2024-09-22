

import turtle
numberofsides = 100

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
turtle.teleport(0,300)
# for i in range (1):
#    turtle.circle(90,150)
#    turtle.forward(30)
#    turtle.left(90)
#    turtle.forward(30)
#    turtle.circle(90,150)
#    turtle.left(90)
#    turtle.forward(30)
#    turtle.circle(90,150)
#    turtle.forward(30)
#       turtle.left(60)
#    turtle.forward(30)
#    turtle.circle(90,180)



  


    




turtle.exitonclick()