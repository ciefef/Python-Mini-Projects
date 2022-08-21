    # -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 19:58:43 2022

@author: Risse
"""

import math 
#C27
#Ask the user to enter a number with lots of
#decimal places. Multiply this number by two and
#display the answer.
num = float (input("Enter a number with lots of decimal places: "))
print (num)

#C28
#Update program 027 so that it will display the answer to
#two decimal places
num = float (input("Enter a number with lots of decimal places: "))
print (round (num, 2))

#C29
#Ask the user to enter an integer that is over 500. Work
#out the square root of that number and display it to two
#decimal places.
num = int (input ("Enter a number over 500: "))
sqrt = math.sqrt (num)
print  (round (sqrt, 2))

#C30
#Display pi (π) to five decimal places.
pi = math.pi
print (round (pi, 5))

#C31
#Ask the user to enter the radius of a circle
#(measurement from the centre point to the edge). Work
#out the area of the circle (π*radius2).
rad = float (input ("Enter the radius of the circle: "))
area = math.pi * rad**2
print (area)

#C32
#Ask for the radius and the depth of a cylinder
#and work out the total volume (circle area*depth) rounded to three decimal places.
rad = float (input ("Enter the radius of the cylinder: "))
depth = float (input ("Enter the depth of the cyclinder: "))
area = math.pi * rad**2
volume = area * depth
print (round (volume, 3))

#C33
#Ask the user to enter two numbers. Use whole number division to divide
#the first number by the second and also work out the remainder and
#display the answer in a user-friendly way (e.g. if they enter 7 and 2 display
#“7 divided by 2 is 3 with 1 remaining”).
num1 = int (input ("Enter the first number: "))
num2 = int (input("Enter the first number: "))
quot = num1 // num2
remain = num1 % num2 
print (num1, "divided by", num2, "is", quot, "remainder", remain)

#C34
#Display the following message:
#    1. Square
#    2. Triangle
#If the user enters 1, then it should ask them for
#the length of one of its sides and display the
#area. If they select 2, it should ask for the base
#and height of the triangle and display the area. If
#they type in anything else, it should give them a
#suitable error message

print ("Choose below: \n 1. Square \n 2. Triangle")
shape = int (input ("1 or 2? "))
if shape == 1:
    side = float (input ("Enter the length of the side of the square: "))
    area = side ** 2
    print ("Area of the square:", area)
elif shape == 2:
    base = float (input ("Enter the base of the triangle: "))
    height = float (input ("Enter the height of the triangle: "))
    area = (base * height)/2
    print ("Area of the triangle:", area)
else:
    print ("Error: Please only choose between 1 or 2")














