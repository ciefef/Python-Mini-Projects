# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 20:19:27 2022

@author: Risse
"""

#C052
#Display a random integer between
#1 and 100 inclusive.
import random
num = random.randint (1, 100)
print (num)

#C053
#Display a random fruit from
#a list of five fruits
import random
fruits = random.choice(["mango", "strawberry", "orange", "banana", "sweet potato", "grapes"])
print (fruits)

#C054
#Randomly choose either heads or tails (“h” or “t”). Ask
#the user to make their choice. If their choice is the same
#as the randomly selected value, display the message
#“You win”, otherwise display “Bad luck”. At the end, tell
#the user if the computer selected heads or tails.
choice = random.choice (["t", "h"])
user = input ("Head or Tail? (t/h): ")
if choice == user:
    print ("You win.")
else:
    print ("Bad Luck")
print ("The computer chooses", choice)

#C055
#Randomly choose a number between 1 and 5. Ask the user to pick a
#number. If they guess correctly, display the message “Well done”,
#otherwise tell them if they are too high or too low and ask them to pick a
#second number. If they guess correctly on their second guess, display
#“Correct”, otherwise display “You lose”.
import random
for i in range (0, 2):
    num = random.randint (1, 5)
    print (num)
    user = int (input("Pick a number: "))
    if user < num:
        print ("Too Low.")
    elif user > num:
        print ("Too high")
    else:
        print ("You win")
        break
if user != num:
    print ("You lose")

#C056
#Randomly pick a whole number between 1 and 10. Ask the user to enter a number and
#keep entering numbers until they enter the number that was randomly picked.
num = random.randint (1, 10)
print(num)
user = int (input("Enter a number: "))
while user != num:
    user = int (input("Enter another number: "))
print ("You got it!")


#C057
#Update program 056 so that it tells the user if they
#are too high or too low before they pick again.
num = random.randint (1, 10)
print(num)
user = int (input("Enter a number: "))
while user != num:
    if user < num:
        print ("Too low.")
        user = int (input("Enter another number: "))
    else:
        print ("Too high")
        user = int (input("Enter another number: "))
print ("You got it!")

#C058
#Make a maths quiz that asks five questions by randomly
#generating two whole numbers to make the question
#(e.g. [num1] + [num2]). Ask the user to enter the
#answer. If they get it right add a point to their score. At
#the end of the quiz, tell them how many they got correct
#out of five.
import random
points = 0
for i in range (0, 5):
    num1 = random.randint (1, 100)
    num2 = random.randint (1, 100)
    cor = num1 + num2
    print ("What is", num1, "added to", num2)
    ans = int (input())
    if ans == cor:
        print ("Correct")
        points = points + 1
    else:
        print ("Wrong")
print ("Your total score is", points)


#C059
#Display five colours and ask the user to pick one. If they
#pick the same as the program has chosen, say “Well
#done”, otherwise display a witty answer which involves
#the correct colour, e.g. “I bet you are GREEN with envy”
#or “You are probably feeling BLUE right now”. Ask
#them to guess again; if they have still not got it right,
#keep giving them the same clue and ask the user to
#enter a colour until they guess it correctly.
import random
colors = random.choice (["red", "blue", "green", "yellow", "purple"])
print ("red")
print ("blue")
print ("green")
print ("yellow")
print ("purple")
user = input ("Choose one color: ")
while colors != user:
    if colors == "green":
        print ("I bet you are GREEN with envy")
        user = input ("Choose one color: ")
    elif colors == "blue":
        print ("You are probably feeling BLUE right now")
        user = input ("Choose one color: ")
    elif colors == "red":
        print ("You are burning red")
        user = input ("Choose one color: ")
    elif colors == "yellow":
        print ("Yellowing sun")
        user = input ("Choose one color: ")
    else:
        print ("purple win")
        user = input ("Choose one color: ")        
if colors == user:
    print ("Well done!")







