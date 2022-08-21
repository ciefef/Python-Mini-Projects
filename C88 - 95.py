# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 19:13:58 2022

@author: Risse
"""

#088
#Ask the user for a list of five integers. Store them in an array.
#Sort the list and display it in reverse order.
from array import *
num = array ('i',[])
for i in range (0, 5):
    user = int (input ("Enter a number: "))
    num.append (user)
num = sorted (num)
num.reverse()
print (num)

#089
#Create an array which will store a list of integers.
#Generate five random numbers and store them in
#the array. Display the array (showing each item on
#a separate line).
from array import *
import random
num = array ('i', [])
for i in range (0, 5):
    ran = random.randint (0, 100)
    num.append(ran)
    print (ran)
for x in num:    
    print (x)

#090
#Ask the user to enter numbers. If they enter a number between 10 and 20, save it in the array,
#otherwise display the message “Outside the range”. Once five numbers have been
#successfully added, display the message “Thank you” and display the array with each item shown
#on a separate line.
from array import *
arr = array ('i', [])
while len(arr) < 5:
    user = int (input ("Enter a number: "))   
    if user >= 10 and user <= 20:
        arr.append(user)
    else:
        print ("Out of range.") 
print ("Thank you.")
for x in arr:
    print (x)    


# 091
# Create an array which contains five numbers (two of which
# should be repeated). Display the whole array to the user. Ask
# the user to enter one of the numbers from the array and
# then display a message saying how many times that number appears in the list.
from array import *
arr = array ('i', [1, 1, 3, 4, 5])
print (arr)
user = int (input ("Enter a number: "))
count = arr.count (user)
print (count)


# 092 
# Create two arrays (one containing three numbers that
# the user enters and one  containing a set of five random
# numbers). Join these two arrays together into one large array.
# Sort this large array and display it so that each number appears
# on a separate line.
from array import *
import random
arr1 = array ('i', [])
arr2 = array ('i', [])
for i in range (0, 3):
    user = int (input("Enter a number: "))
    arr1.append (user)
for i in range (0, 5):
    ran = random.randint (0, 100)
    arr2.append (ran)
arr1.extend (arr2)
for x in arr1:
    print (x)
    

# 093
# Ask the user to enter five numbers. Sort them into order
# and present them to the user. Ask them to select one of the
# numbers. Remove it from the original array and save it in a
# new array.
from array import *
arr1 = array ('i', [])
for i in range (0, 5):
    user = int (input ("Enter a number: "))
    arr1.append (user)
arr1 = sorted (arr1)
for x in arr1:    
    print (x)
rev = int (input ("Enter a number to remove: "))
if rev in arr1:
    arr1.remove(rev)
    arr2 = array('i', [])
    arr2.append (rev)
else:
    print ("Not in the list.")


# 094
# Display an array of five numbers. Ask the user to
# select one of the numbers. Once they have selected a
# number, display the position of that item in the
# array. If they enter something that is not in
# the array, ask them to try again until they select a
# relevant item.
from array import *
arr1 = array ('i', [3, 4, 6, 7, 9])
for x in arr1:
    print (x)
user = int (input ("Choose one number: "))
if user in arr1:
    pos = arr1.index(user)
    print ("The position of your number is", pos)
else:
    user = int (input ("Please enter a number that is in the list."))

# 095
# Create an array of five numbers between 10 and 100 which each have
# two decimal places. Ask the user to enter a whole number between 2 and 5.
# If they enter something outside of that range, display a suitable error message
# and ask them to try again until they enter a valid amount. Divide each of the
# numbers in the array by the number the user entered and display the answers
# shown to two decimal places.
from array import *
arr1 = array ('f', [33.33, 44.44, 55.55, 66.66, 77.77])
for x in arr1:
    print (x)
tryagain = True
while tryagain == True:
    user = int (input ("Enter a whole number between 2 and 5: "))
    if  user < 2 or user > 5:
        print ("Incorrect value, try again.")
    else:
        tryagain = False
for i in range (0, 5):
  ans = round (arr1[i] / user, 2)
  print (ans)
        



















