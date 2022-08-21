# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 22:40:46 2022

@author: Risse
"""

import turtle
turtle.shape("turtle")
for i in range (0, 5):
    turtle.forward (100)
    turtle.right (72)
turtle.exitonclick ()

import turtle 
for i in range (0, 10):
    turtle.right (36)
    for i in range (0,5):
        turtle.forward (100)
        turtle.right (72)
turtle.exitonclick()

#C060
#Draw a square.
import turtle
for  i in range (0, 4):
    turtle.forward (100)
    turtle.right (90)
turtle.exitonclick()

#C061
#Draw a triangle.
import turtle
for  i in range (0, 3):
    turtle.forward (100)
    turtle.right (120)
turtle.exitonclick()

#C062
#Draw a circle.
import turtle
for  i in range (0, 360):
    turtle.forward (1)
    turtle.right (1)
turtle.exitonclick()
7
#C063
#Draw three squares
#in a row with a gap
#between each. Fill
#them using three
#different colours
import turtle
turtle.color ("black", "red")
turtle.begin_fill()
for i in range (0, 4):
    turtle.forward(100)
    turtle.right (90)
turtle.penup ()
turtle.end_fill ()
turtle.forward (100)
turtle.color ("black", "yellow")
turtle.begin_fill()
for i in range (0, 4):
    turtle.forward(100)
    turtle.right (90)
turtle.penup ()
turtle.end_fill ()
turtle.forward (100)
turtle.color ("black", "green")
turtle.begin_fill()
for i in range (0, 4):
    turtle.forward(100)
    turtle.right (90)
turtle.penup ()
turtle.end_fill ()
turtle.exitonclick()


#064
#Draw a five-pointed star.
import turtle
for i in range (0, 5):
    turtle.forward (100)
    turtle.right (144)
turtle.exitonclick()




#C065
#Write the numbers as shown below,
#starting at the bottom of the number
#one.
import turtle
turtle.left (90)
turtle.forward (100)
turtle.penup ()
turtle.right (90)
turtle.forward (50)
turtle.pendown()
turtle.forward (100)
turtle.right (90)
turtle.forward (50)
turtle.right (90)
turtle.forward (100)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (100)
turtle.penup ()
turtle.forward (50)
turtle.pendown()
turtle.forward (100)
turtle.left(90)
turtle.forward (50)
turtle.left(90)
turtle.forward (50)
turtle.penup ()
turtle.left(180)
turtle.forward (50)
turtle.pendown()
turtle.left(90)
turtle.forward (50)
turtle.left(90)
turtle.forward (100)
turtle.exitonclick()

#066
#Draw an octagon that uses a different colour (randomly
#selected from a list of six possible colours) for each line.
import turtle
import random
for i in range (0, 8):
    colors = random.choice (["green", "red", "blue", "orange", "yellow", "violet"])
    turtle.color(colors)
    turtle.forward (50)
    turtle.right (45)
turtle.exitonclick()

#067
#Create the following pattern:
import turtle
for x in range (0,10):
    for i in range (0, 8):
        turtle.forward (50)
        turtle.right(45)
    turtle.right (36)
turtle.exitonclick()
        

068
#Draw a pattern that will change each time the
#program is run. Use the random function to pick
#the number of lines, the length of each line and
#the angle of each turn.
import random
import turtle
lines = random.randint (5, 20)
lenght = random.randint (1, 100)
angle = random.randint (1, 365)
for i in range (0, lines):
    turtle.forward (lenght)
    turtle.right (angle)
turtle.exitonclick()


