# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
turtle.Screen().bgcolor ("Navy")
t.speed (10)

t.penup()
t.goto (0,0)
t.pendown()
t.color("cyan")



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
