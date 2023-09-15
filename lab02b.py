## Author: Ahmad Dzulfikar As Shavy
## File name: lab02b.py
## using turtle to draw regular polygons
import turtle

# make the turtle invisible
turtle.hideturtle()

turtle.shape('turtle')
turtle.title('Lab 02')
# get the number of sides from user
n = int(turtle.textinput("Lab 02", "The number of sides: "))
# the length of a side is getting shorter as n getting larger
# When n = 4, the length of a side is 100.
side_length = 400/n
interior = 180 * (n - 2) / n

# get the value of red color from user
r = float(turtle.textinput("Lab 02",
"The red color component [between 0 and 1]: "))
# get the value of green color from user
g = float(turtle.textinput("Lab 02",
"The green color component [between 0 and 1]: "))
# get the value of blue color from user
b = float(turtle.textinput("Lab 02",
"The blue color component [between 0 and 1]: "))

# draw a polygon
polygon = turtle.Turtle()
polygon.up()
polygon.goto(-180,0)
polygon.down()
for p in range(n):
    polygon.forward(side_length)
    polygon.left(180 - interior) 

# create the color from rgb values given by user
turtle.color(r,g,b)

# draw a regular polygon with n sides and color(r,g,b)
polygon = turtle.Turtle()
polygon.up()
polygon.goto(220,0) # move the turtle to a new location
polygon.down()
polygon.color(r,g,b)
polygon.begin_fill()
# polygon.color("green")
for p in range(n):
    polygon.forward(side_length)
    polygon.left(180 - interior) 
polygon.end_fill()

# for exit
turtle.up()
turtle.goto(0,-100)
turtle.down()
turtle.color('blue')
turtle.write("Please click on the graphics window to exit ...",
False, align='center', font=('Arial', 20, 'normal'))

# wait for user to click on the screen to exit
turtle
# the end
turtle.exitonclick()
turtle.done()

# Collabolator: chatGPT