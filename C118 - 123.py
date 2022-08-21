# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 08:58:47 2022

@author: Risse
"""

# 118
# Define a subprogram that will ask the user to
# enter a number and save it as the variable
# “num”. Define another subprogram that will
# use “num” and count from 1 to that number
def user_num ():
    num = int (input ("Enter a number: "))
    return num
def count (num):
    for i in range (0, num):
        print (i + 1)
def main ():
    num = user_num()
    count (num)
main ()

# 119
# Define a subprogram that will ask the user to pick a low and a 
# high number, and then generate a random number between those
# two values and store it in a variable called “comp_num”. Define 
# another subprogram that will give the instruction “I am thinking 
# of a number…” and then ask the user to guess the number they
# are thinking of. Define a third subprogram that will check to see 
# if the comp_num is the same as the user’s guess. If it is, it 
# should display the message “Correct, you win”, otherwise it 
# should keep looping, telling the user if they are too low or
# too high and asking them to guess again until they guess correctly.
import random
def comp ():
    num = input ("The number is high or low? (h/l) ")
    if num == "h":
        comp_num = random.randint (50, 100)
    elif num == "l":
        comp_num = random.randint (0, 49)
    else:
        print ("Please only choose between high or low. (h/l) ")
    return comp_num
def user ():
    print ("I am thinking of a number... ")
    user_num = int (input ("Enter the number you're thinking of: "))
    return user_num
def compare ():
    comp_num = comp ()
    user_num = user ()
    while comp_num != user_num:
        if user_num > comp_num :
            print ("Your number is too high")
        else:
            print ("Your number is too low")
        user_num = user ()
    print ("Correct! You win!")   
compare ()
    
# 120
# Display the following menu to the user:
# If they enter a 1, it should run a subprogram that will
# generate two random numbers between 5 and 20, and
# ask the user to add them together. Work out the correct
# answer and return both the user’s answer and the
# correct answer.
# If they entered 2 as their selection on the menu, it
# should run a subprogram that will generate one number
# between 25 and 50 and another number between 1 and
# 25 and ask them to work out num1 minus num2. This
# way they will not have to worry about negative answers.
# Return both the user’s answer and the correct answer.
# Create another subprogram that will check if the user’s
# answer matches the actual answer. If it does, display
# “Correct”, otherwise display a message that will say
# “Incorrect, the answer is” and display the real answer.
# If they do not select a relevant option on the first menu
# you should display a suitable message.
import random
def add_num ():
    num1 = random.randint (5, 20)
    num2 = random.randint (5, 20)
    question = str (num1) +  " + " + str (num2) + " = "
    user_ans = int (input (question))
    real_ans = num1 + num2
    data = (user_ans, real_ans)
    return data
def sub_num ():
    num1 = random.randint (25, 50)
    num2 = random.randint (1, 25)
    question = str (num1) +  " - " + str (num2) + " = "
    user_ans = int (input (question))
    real_ans = num1 - num2
    data = (user_ans, real_ans)
    return data
def compare (user_ans, real_ans):
    if user_ans == real_ans:
        print ("Correct!")
    else:
        priint ("Incorrect, the answer is", real_ans)
def main ():
    print ("1. Addition")
    print ("2. Subtraction")
    choice = int (input ("Enter 1 or 2: "))
    if choice == 1:
        user_ans, real_ans = add_num ()
        compare (user_ans, real_ans)
    elif choice == 2:
        user_ans, real_ans = sub_num ()
        compare (user_ans, real_ans)
    else:
        print ("Please only choose between 1 or 2: ")
main ()

# 121
# Create a program that will allow the user to easily manage a list 
# of names. You should display a menu that will allow them to add a 
# name to the list, change a name in the list, delete a name from 
# the list or view all the names in the list. There should also be a
# menu option to allow the user to end the program. If they select an 
# option that is not relevant, then it should display a suitable 
# message. After they have made a selection to either add a name, 
# change a name, delete a name or view all the names, they should 
# see the menu again without having to restart the program. The 
# program should be made as easy to use as possible.
names_list = []
def display (names_list):
    for i in range (0, len(names_list)):
        print (names_list [i])
        
def add (names_list):
    name = input ("Enter the name you want to add: ")
    names_list.append (name)
    return name_list

def remove (names_list):
    name = input ("Enter the name you want to remove: ")
    names_list.remove (name)
    return names_list

def change (names_list):
    pos = int (input ("Enter the position you want to change"))
    name = input ("Enter the name you want to change into: ")
    names.list [pos] = name
    return names.list 

def end_prog ():
    exit ()
    
def menu ():
    print  ("What do you want to do? ")
    print ("1. Display the list")
    print ("2. Add data")
    print ("3. Remove a name")
    print ("4. Change the data")
    print ("5. End the program")
    choice = int (input ("What do you want to do? "))
    return choice

def main ():
    choice = menu ()
    while choice != 5:
        if choice == 1:
            display (names_list)
            choice = menu ()
        elif choice == 2:
            add (names_list)
            choice = menu ()
        elif choice == 3:
            remove (names_list)
            choice = menu ()
        elif choice == 4:
            change (names_list)
            choice = menu ()
        else:
            print ("Please enter only between 1 to 5") 
    if choice == 5:
        end_prog ()    
    
main ()   

# 122
# Create the following menu:
# If the user selects 1, allow them to add to a file
# called Salaries.csv which will store their name
# and salary. If they select 2 it should display all
# records in the Salaries.csv file. If they select 3 it
# should stop the program. If they select an
# incorrect option they should see an error
# message. They should keep returning to the
# menu until they select option 3.
import csv
file = open ("Salaries.csv", "w")
file.close ()
def add ():
    file = open ("Salaries.csv", "a")
    name = input ("Enter the name: ")
    salary = int (input ("Enter your salary: "))
    new_record = name + "," + str(salary)
    file.write (new_record)
    file.close ()
def display ():
    file = open ("Salaries.csv", "r")
    for row in file:
        print (row)
    file.close ()
def end_prog ():
    quit ()
def menu ():
    print ("1. Add to file")
    print ("2. View all records")
    print ("3. Quit program")
    choice = int (input ("Enter the number of your selection: "))
    return choice
def main ():
    choice = menu ()
    while choice != 3:
        if choice == 1:
            add ()
            choice = menu ()
        elif choice == 2:
            display ()
            choice = menu ()
        else: 
            print ("Please enter the appropriate selection: ")
    end_prog ()

main ()

    
# 123
# In Python, it is not technically possible to directly
# delete a record from a .csv file. Instead you need
# to save the file to a temporary list in Python,
# make the changes to the list and then overwrite
# the original file with the temporary list.
# Change the previous program to allow you to do
# this. Your menu should now look like this:

import csv
file = open ("Salaries.csv", "w")
file.close ()
def add ():
    file = open ("Salaries.csv", "a")
    name = input ("Enter the name: ")
    salary = int (input ("Enter your salary: "))
    new_record = name + "," + str(salary)
    file.write (new_record)
    file.close ()
def display ():
    file = open ("Salaries.csv", "r")
    for row in file:
        print (row)
    file.close ()
def delete ():
    file = open ("Salaries.csv", "r")
    x = 0
    tmp = []
    for row in file:
        tmp.append (row)
    file.close ()
    for row in tmp:
        print (x, row)
    getRid = int (input ("Enter the row you want delete"))
    del tmp [getRid]
    file = open ("Salaries,csv", "w")
    for row in tmp:
        file.write (row)
    file.close ()
def end_prog ():
    quit ()
def menu ():
    print ("1. Add to file")
    print ("2. View all records")
    print ("3. Delete a record")
    print ("4. Quit the program")
    choice = int (input ("Enter the number of your selection: "))
    return choice
def main ():
    choice = menu ()
    tryagain = True
    while tryagain == True:
        if choice == 1:
            add ()
            choice = menu ()
        elif choice == 2:
            display ()
            choice = menu ()
        elif choice == 3:
            delete ()
        elif choice == 4:
            end_prog ()
            tryagain = False
        else: 
            print ("Please enter the appropriate selection")
main ()










