# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 21:00:34 2022

@author: Risse
"""

#C35
#Ask the user to enter their name and then
#display their name three times.
name = input ("Enter your name: ")
for i in range (1, 4):
    print (name)

#C36
#Alter program 035 so that it will ask the user to enter their
#name and a number and then display their name that
#number of times.
name = input ("Enter your name: ")
times = int (input ("Enter the number of iterations: "))
for i in range (1, times+1):
    print (name)
    
#C37
#Ask the user to enter their name and display each letter in
#their name on a separate line.
name = input ("Enter your name: ")
for i in name:
    print (i)
    

#C38
#Change program 037 to also ask for a number. Display their name (one
#letter at a time on each line) and repeat this for the number of times
#they entered
name = input ("Enter your name: ")
times = int (input ("Enter the number of iterations: "))
for j in range (1, times+1):
    for i in name:
        print (i)

#C39
#Ask the user to enter a number between 1
#and 12 and then display the times table for that number.
num = int (input ("Enter a number between 1 and 12: "))
for i in range (1, 13):
    print (num * i)

#C40
#Ask for a number below 50 and then count down from
#50 to that number, making sure you show the number
#they entered in the output.

num = int (input ("Enter a number below 50: "))
for i in range (num, 0, -1):
    print (i)

#C41 
#Ask the user to enter their name and a number. If the
#number is less than 10, then display their name that
#number of times; otherwise display the message “Too
#high” three times.

name = input ("Enter your name: ")
num = int(input ("Choose a number: "))
if num < 10  :
    for i in range (1, num+1):
        print (name)
else:
    for i in range (1, 4):
        print ("Too High")
     
#C42        
#Set a variable called total to 0. Ask the user to enter
#five numbers and after each input ask them if they
#want that number included. If they do, then add the
#number to the total. If they do not want it included,
#don’t add it to the total. After they have entered all five
#numbers, display the total.        
total = 0; 
for i in range (1, 6):
    num = int (input("Choose a number: "))
    inc = int (input ("Do you want it to be included? \n 1. Yes \n 2. No \n Answer: "))
    if inc == 1:
        total = total + num
    else:
        total = total
print (total)

#C43
#Ask which direction the user wants to count (up or down). If they select up, then ask
#them for the top number and then count from 1 to that number. If they select down, ask
#them to enter a number below 20 and then count down from 20 to that number. If they
#entered something other than up or down, display the message “I don’t understand”.
direc = input("Which direction do you want to count, up or down? (u/d) ")
direc = direc.lower ()
if direc == "u":
    num = int (input ("Enter the top number: "))
    for i in range (1, num+1):
        print (i)
elif direc == "d":
    num = int (input("Enter a number below 20"))
    for i in range (20, num-1, -1):
        print (i)
else:
    print ("I don't understand")

#C44
#Ask how many people the user wants to invite to a party. If they enter a number below
#10, ask for the names and after each name display “[name] has been invited”. If they
#enter a number which is 10 or higher, display the message “Too many people”.
num  = int (input("Enter the number of people you'll invte to a party: "))
if num < 10:
    for i in range (1, num+1):
        name = input ("Enter the name: ")
        print (name, "has been invited.")
else:
    print ("Too may people")    



























