# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:54:58 2022

@author: Risse
"""

# 105
# Write a new file called “Numbers.txt”. Add five numbers
# to the document which are stored on the same line
# and only separated by a comma. Once you have run the program, look in
# the location where your program is stored and you
# should see that the file has been created. The
# easiest way to view the contents of the new text file
# on a Windows system is to read it using Notepad.
file = open ("Numbers.txt", "w")
file.write ("1, 2, 3, 4, 5.")
file.close()

# 106
# Create a new file called “Names.txt”. Add five names to the
# document, which are stored on separate lines. Once you have
# run the program, look in the location where your program is
# stored and check that the file has been created properly.
file = open ("Names.txt", "w")
file.write ("So Min \n")
file.write ("Mudeok \n")
file.write ("Bu yeon \n")
file.write ("Jang uk \n")
file.write ("Seo yul \n")
file.close()

# 107
# Open the Names.txt file and
# display the data in Python.
file = open ("Names.txt", "r")
print (file.read ())

# 108
# Open the Names.txt file. Ask the user to input a
# new name. Add this to the end of the file and
# display the entire file.
file = open ("Names.txt", "a")
user = input ("Add new name: ")
file.write (user + "\n")
file.close()
file = open ("Names.txt", "r")
print (file.read ())
file.close()

# 109
# Display the following menu to the user:
# Ask the user to enter 1, 2 or 3. If they select
# anything other than 1, 2 or 3 it should display a
# suitable error message.
# If they select 1, ask the user to enter a school
# subject and save it to a new file called
# “Subject.txt”. It should overwrite any existing file
# with a new file.
# If they select 2, display the contents of the
# “Subject.txt” file.
# If they select 3, ask the user to enter a new
# subject and save it to the file and then display
# the entire contents of the file.
# Run the program several times to test the
# options.
print ("1. Create a new file \n")
print ("2. Display the file \n")
print ("3. Add new item to the file \n")
user = int ( input ("Make a selection 1, 2, or 3: "))
if user == 1:
    file = open ("Subject.txt", "w")
    subject = input ("Enter a subject: ")
    file.close ()
    file = open ("Subject.txt", "a")
    file.write (subject)
    file.close ()
elif user == 2:
    file = open ("Subjects", "r")
    print (file.read())
    file.close ()
elif user == 3:
    file = open ("Subject.txt", "w")
    subject = input ("Enter new subject: ")
    file.close ()
    file = open ("Subject.txt", "a")  
    file.write (subject)
    file.close ()
    file = open ("Subject.txt", "r")
    print (file.read())
    file.close ()
else:
    print ("Please only choose between 1, 2, or 3")      


# 110
# Using the Names.txt file you created earlier, display the list of
# names in Python. Ask the user to  type in one of the names and then
# save all the names except the one they entered into a new file called
# Names2.txt.
file = open ("Names.txt", "r")
print (file.read ())
file.close ()
file = open ("Names.txt", "r")
user = input ("Enter the name: ")
user = user + "\n"
for row in file:
    if row != user:
        file = open ("Names2.txt", "a")
        newname = row
        file.write (newname)
        file.close ()
file.close ()


































