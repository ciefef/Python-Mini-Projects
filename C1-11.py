# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 19:59:57 2022

@author: Risse
"""

#Challenges 1 - 11 pp.22
#01
#Ask for the user’s first name and display 
#the output messageHello [First Name]
name = input ("Enter your first name: ")
print ("Hello", name)

#02
#Ask for the user’s first name and then ask 
#for their surname and display the output 
#message Hello [First Name] [Surname].
firstname = input ("Enter your first name: ")
lastname = input ("Enter your last name: ")
print ("Hello", firstname, lastname)

#03
#Write code that will display the joke 
#“What do you call a bear with no teeth?” 
#and on the next line display the answer 
#“A gummy bear!” Try to create it using 
#only one line of code.
print ("What do you call a bear with no teeth? \nA gummy bear!")

#04
#Ask the user to enter two numbers. Add 
#them together and display the answer 
#as The total is [answer].
num1 = int(input("Enter the first number: "))
num2 = int (input ("Enter the second number: "))
print ("The total answer is: ", num1 + num2)

#05
#Ask the user to enter three numbers. 
#Add together the first two numbers and 
#then multiply this total by the third. 
#Display the answer as The answer is [answer].
num1 = int (input ("Enter the first number: "))
num2 = int (input ("Enter the second number: "))
num3 = int (input ("Enter the third number: "))
print ("The answer is ", (num1 + num2)*num3)

#06
#Ask how many slices of pizza the user 
#started with and askhow many slicesthey 
#have eaten. Work out how many slices they
#have left and display the answer in a user friendly format.
initial = int (input ("How many slices does your pizza has? "))
eaten = int (input("How many have you eaten? "))
print ("Yayyy! You still have", initial - eaten, "slices of pizza")

#07
#Ask the user for their name and their age. Add 1 to their age
#and display the output [Name] next birthday you
#will be [new age].
name = input ("Hi, what is you name? ")
age = int (input ("Can you tell me your age? "))
print (name," next birthday you wiil be ", age+1)

#08
#Ask for the total price of the bill, then ask how
#many diners there are. Divide the total bill by the
#number of diners and show how much each
#person must pay.
totalprice = int (input ("How much is the total bill? "))
diners = int(input("How many are the diners? "))
bill = totalprice/diners
print ("Each person shall pay ", bill)



#09
#Write a program  that will ask for a number of days 
#and then will show how many hours, minutes and seconds 
#are in that number of days.
days = int (input ("Number of days: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60 
print ("In ", days, " days there are", hours, 
       "hours, ", minutes, "minutes, and ", seconds, "seconds." )

#10
#There are 2,204 pounds in a kilogram. Ask the
user to enter a weight in kilograms and convert it
to pounds.
kg = int (input ("Weight in kg: "))
pounds = kg * 2204
print ("There are ", pounds, "pounds in", kg, "kg.")


#011
#Task the user to enter a number over 100 and then enter a number under
#10 and tell them how many times the smaller number goes into the larger
#number in a user-friendly format.
largernum = int (input("Choose a number greater than 100. "))
smallnum = int (input("Now, choose a number less than 10. "))
print ("Cool! Over", largernum / smallnum, smallnum,"'s can fit into ", largernum)

















