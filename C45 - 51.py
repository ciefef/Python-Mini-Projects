# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 21:49:04 2022

@author: Risse
"""

#C45
#Set the total to 0 to start with. While the total is 50 or less, ask
#the user to input a number. Add that number to the total and
#print the message “The total is… [total]”. Stop the loop when
#the total is over 50.

total = 0 
while total <= 50:
    num = int (input("Enter a number: "))
    total = total + num
    print ("The total is", total)
    
 #C46   
#Ask the user to enter a number. Keep
#asking until they enter a value over 5 and
#then display the message “The last
#number you entered was a [number]” and
#stop the program    
num = int (input ("Enter a number: "))
while num < 5:
    num = int (input ("Enter a new number: "))
print ("The last number you've entered is", num)    
   
#C47
#Ask the user to enter a number and then enter
#another number. Add these two numbers together and
#then ask if they want to add another number. If they
#enter “y", ask them to enter another number and keep
#adding numbers until they do not answer “y”. Once the
#loop has stopped, display the total.

num1 = int (input("Enter the first number: "))
num2 = int (input ("Enter the second number: "))
sum1 = num1 + num2
q1 = input ("Do you want to add another number? (y/n) ")
while q1 == "y":
    num3 = int (input ("Enter another number" ))
    sum1 = sum1 + num3
    q1 = input ("Do you want to add another number? (y/n) ")
print ("The total number is", sum1)

#048
#Ask for the name of somebody the user wants to invite
#to a party. After this, display the message “[name] has
#now been invited” and add 1 to the count. Then ask if
#they want to invite somebody else. Keep repeating this
#until they no longer want to invite anyone else to the
#party and then display how many people they have coming to the party.
name = input ("Enter a name: " )
count = 0
print (name, "has been invited")
count = count + 1
q1 = input ("Do you want to invite other people (y/n) ")
while q1 == "y":
    name = input ("Enter the name: ")
    print (name, "has been invited")
    count = count + 1
    q1 = input ("Do you want to invite other people (y/n) ")
print (count, "people has been invited to the party")
    

#049
#Create a variable called compnum and set the value
#to 50. Ask the user to enter a number. While their guess
#is not the same as the compnum value, tell them if
#their guess is too low or too high and ask them to have
#another guess. If they enter the same value as
#compnum, display the message “Well done, you took [count] attempts”.
count = 0
compnum = 50
num = int(input("Enter a number: "))
count = count + 1
while num != compnum:
    if num < 50:
        print ("Your number is too low")
        num = int (input("Guess another number: "))
        count = count + 1
    if num > 50:
        print ("Your number is too high")
        num = int (input ("Guess another number: "))
        count = count + 1
        
if num == compnum:
    print ("Well done, you took", count, "attempts")


#050
#Ask the user to enter a number between 10 and 20. If they enter a value under 10,
#display the message “Too low” and ask them to try again. If they enter a value
#above 20, display the message “Too high” and ask them to try again. Keep repeating
#this until they enter a value that is between 10 and 20 and then display the
#message “Thank you”.
num = int (input("Enter a number between 10 and 20: "))
while num < 10 or num > 20:
    if num < 10:
        print ("The number is too low.")
        num = int (input("Enter another number: "))
    if num > 20:
        print ("The number is too high.")
        num = int (input("Enter another number: "))
if num >= 10 and num <= 20:
    print ("Thank you.")

#C51
#Using the song “10 green bottles”, display the lines “There are [num] green bottles
#hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle
#should accidentally fall”. Then ask the question “how many green bottles will be
#hanging on the wall?” If the user answers correctly, display the message “There will be
#[num] green bottles hanging on the wall”. If they answer incorrectly, display the
#message “No, try again” until they get it right. When the number of green bottles gets
#down to 0, display the message “There are no more green bottles hanging on the wall”.
num = 10 
while num > 0:
    print ("There are" , num, "green bottles hanging on the wall.")
    print (num, "green bottles hanging on the wall.")
    print ("And if 1 green bottle should accidentally fall")
    num = num - 1
    ans = int (input ("How many green bottles will be hanging on the wall? "))
    if ans == num:
        print ("There are" , num, "green bottles hanging on the wall.")
    while ans != num:
        print ("No, try again")
        ans = int (input ("No, try again: "))
print ("There are no more green bottles hanging on the wall.")































