# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 20:45:01 2022

@author: Risse
"""

# 096
# Create the following using a simple 2D list using the
# standard Python indexing:
data = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

# 097
# Using the 2D list from program 096, ask the user to
# select a row and a column and display that value.
data = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int (input("Enter the row: "))
col = int (input ("Enter the column: "))
print (data [row][col])


# 098
# Using the 2D list from program 096, ask the user
# which row they would like displayed and display
# just that row. Ask them to enter a new value and
# add it to the end of the row and display the row
# again.
data = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int (input ("Enter the row: "))
print (data [row])
new_val = int (input ("Enter a number: "))
data[row].append(new_val)
print (data [row])

# 099 .
# Change your previous program to ask the user which row they
# want displayed. Display that row. Ask which column in that
# row they want displayed and display the value that is held
# there. Ask the user if they want to change the value. If they do,
# ask for a new value and change the data. Finally, display the
# whole row again.
data = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int (input ("Enter the row: "))
print (data [row])
col = int (input ("Enter the column: "))
print (data [row][col])
ask = input ("Do you want to change it? (y/n)")
if ask == "y":
    new_val = int (input ("Enter the number: "))
    data[row][col] = new_val
print (data [row])

# 100
# Create the following using a 2D dictionary showing
# the sales each person has made in the different
# geographical regions:
sales = {"John":{"N":3056, "S":8463, "E":8441, "W":2694}, 
         "Tom":{"N":4832, "S":6786, "E":4737, "W":3612},
         "Anne":{"N":5239, "S":4802, "E":5820, "W":1859},
         "Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}
         }
# 101
# Using program 100, ask the user for a name and a region. Display the relevant data. Ask
# the user for the name and region of data they want to change and allow them to make
# the alteration to the sales figure. Display the sales for all regions for the name they
# choose. 
sales = {"John":{"N":3056, "S":8463, "E":8441, "W":2694}, 
         "Tom":{"N":4832, "S":6786, "E":4737, "W":3612},
         "Anne":{"N":5239, "S":4802, "E":5820, "W":1859},
         "Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}
         }
name = input ("Enter the name: ")
region = input ("Enter the region: ")
print (sales [name][region])
new_val = int (input ("Enter the value: "))
sales [name][region] = new_val
print(sales[name])

# 102
# Ask the user to enter the name, age and shoe size for four
# people. Ask for the name of one of the people in the list and
# display their age and shoe size.
list = {}
for i in range (0, 4):
    name = input ("Enter the name: ")
    age = int (input ("Enter the age: "))
    shoe = int (input ("Enter the show size: "))
    list [name] = {"Age":age, "Shoe size":shoe} 
ask = input ("Enter the name: ")
print (list[ask])

# 103
# Adapt program 102 to display the
# names and ages of all the people in
# the list but do not show their shoe
# size
list = {}
for i in range (0, 4):
    name = input ("Enter the name: ")
    age = int (input ("Enter the age: "))
    shoe = int (input ("Enter the show size: "))
    list [name] = {"Age":age, "Shoe size":shoe} 
for name in list:
    print ((name), list[name]["Age"])


# 104
# After gathering the four names, ages and shoe sizes, ask the
# user to enter the name of the person they want to remove from
# the list. Delete this row from the data and display the other rows
# on separate lines.
list = {}
for i in range (0, 4):
    name = input ("Enter the name: ")
    age = int (input ("Enter the age: "))
    shoe = int (input ("Enter the show size: "))
    list [name] = {"Age":age, "Shoe size":shoe} 
rem = input ("Enter the name you want to remove: ")
del list [rem]
for name in list:
    print ((name), list [name])




















