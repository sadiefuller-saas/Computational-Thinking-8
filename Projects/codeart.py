# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
turtle.Screen().bgcolor ("Navy")
#this changed the background to navy
t.speed (10)
#this changed the speed to 10

t.goto (0,0)
t.pendown()
t.color("cyan")
#this changed the color to cyan


for i in range (67) :
    t.forward (150 + 2*i)
    t.left (200)
    t.forward (150 + 2*i)
    t.left (200)

t = turtle.Turtle()

t.speed (10)
#this changed the speed to 10

t.goto (0,0)
t.pendown()
t.color("cyan")
#this changed the color to cyan


for i in range (67) :
    t.forward (150 + 2*i)
    t.left (200)
    t.forward (150 + 2*i)
    t.left (200)

turtle.exitonclick ()




# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
