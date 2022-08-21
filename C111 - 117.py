# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 21:16:16 2022

@author: Risse
"""

# 111
# Create a .csv file that will store the following data. Call it “Books.csv”.
import csv
file = open ("Books.csv", "w")
newRecord = "To Kill A Mockingbird, Harper Less, 1960 \n"
file.write (str(newRecord))
newRecord = "A Brief History of Time, Stephen Hawking, 1988 \n"
file.write (str(newRecord))
newRecord = "The Great Gatsby, F.Scott Fritgerald, 1922 \n"
file.write (str(newRecord))
newRecord = "The man who mistook Hist Wife for a Hat, Oliver Sacks, 1985 \n"
file.write (str(newRecord))
newRecord = "Pride and Prejudice, Jan Austen, 1813 \n"
file.write (str(newRecord))
file.close ()

# 112
# Using the Books.csv file from program 111, ask
# the user to enter another record and add it to the
# end of the file. Display each row of the .csv file
# on a separate line.
import csv
file = open ("Books.csv", "w")
title = input ("Enter the title of the book: ")
author = input ("Enter the author: ")
date = input("Enter the date: ")
new = title + "," + author + "," + date + "\n"
file.write (str (new))
file.close()
file = open ("Books.csv", "r")
for row in file:
    print (row)
file.close ()

# 113
# Using the Books.csv file, ask the user how many records
# they want to add to the list and then allow them to add
# that many. After all the data has been added, ask for an
# author and display all the books in the list by that author.
# If there are no books by that author in the list, display a
# suitable message.
import csv
num = int (input ("How many record you want to add? "))
while num > 0:
    file = open ("Books.csv", "w")
    title = input ("Enter the title of the book: ")
    author = input ("Enter the author: ")
    date = input("Enter the date: ")
    new = title + "," + author + "," + date + "\n"
    file.write (str (new))
    file.close()
    num = num - 1
file = open ("Books.csv", "r")
search = input ("Enter the author: ")
reader = csv.reader (file)
for row in file:
    if search in str (row):
        print (row)

# 114
# Using the Books.csv file, ask the user
# to enter a starting year and an end
# year. Display all books released
# between those two years.    
import csv
start_year = int ( input ("Enter starting year: "))
end_year =  int (input ("Enter the end year: "))
file = list (csv.reader (open("Books.csv")))
tmp = []
for row in file:
    tmp.append (row)
x = 0
for row in tmp:
    if int (tmp[x][2]) >= start_year and int (tmp[x][2]) <= end_year:
        print (tmp[x])
    x = x+1

# 115
# Using the Books.csv file, display the data in
# the file along with the row number of each.
import csv
file = open ("Books.csv", "r")
x = 0
for row in file:
    display = "Row: " + str (x) + "-" + row
    print (display)
    x = x+1

# 116
# Import the data from the Books.csv file into a list. Display the
# list to the user. Ask them to select which row from the list
# they want to delete and remove it from the list. Ask the user
# which data they want to change and allow them to change it.
# Write the data back to the original .csv file, overwriting the
# existing data with the amended data.
file = list (csv.reader(open("Books.csv")))
booklist = []
for row in file:
    booklist.append (row)
x = 0            
for row in booklist:
    display = x, booklist [x]
    print (display)

getrid = int (input ("Enter which row you want to delete: "))
del booklist [getrid] 
change = int (input ("Enter which row you want to change: "))
x = 0
for row in booklist[change]:
    display =  x, booklist [alter][x]
    print (display)
    x = x+1
part = int input ("Which part do you want to change? ")
newData = input ("Enter new data: ")
booklist [alter][part] = newData
print ([booklist][alter])

file = open ("Books.csv", "w")
x = 0
for row in booklist:
    newRecord = booklist [x][0] + "," + booklist
    file.write (newrecord)
    x = x+1
file.close()

# 117
# Create a simple maths quiz that will ask the user for their name and then generate two
# random questions. Store their name, the questions they were asked, their answers and
# their final score in a .csv file. Whenever the program is run it should add to the .csv file
# and not overwrite anything.
import csv
import random
file = open ("mathQuiz.csv", "w")
name = input ("Enter your name: ")
newrec = name
operator = ["+", "-", "/", "*"]
for i in range (0, 2):
    num1 = random.randint (0, 100)
    num2 = random.randint (0, 100)
    sign = random.choice (operator)
    question [i] = str (num1) + sign + str (sign) + "="
    print (question[i])
    answer = int (input ("Enter your answer: "))
    op = sign
    realans = num1, op, num2
    if answer == realans:
        score = score + 1
    newrec = name ""
newRec = name + "," + question
file.close ()

import csv
import random
score = 1
name = input ("Enter your name: ")
num1 = random.randint (1,100)
num2 = random.randint (1, 100)
q1 =  str  (num1) + " + " + str (num2) + " = "
ans1 = int (input ("question"))
realans = num1 + num2
if ans1 == realans:
    score = score + 1
num3 = random.randint (1, 100)
num4 = random.randint (1, 100)
q2 = str  (num3) + " + " + str (num4) + " = "
ans1 = int (input ("question"))
realans = num3 + num4
if ans1 == realans:
    score = score + 1
file = open ("MathQuiz", "a")
newrecord = name + "," + q1 + "," + str (ans1) + "," + q2 + "," + str (ans2) + "," + str(score) + "\n"
file.write (str(newrecord))
file.close ()




























