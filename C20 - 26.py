# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:03:54 2022

@author: Risse
"""

#C020
#Ask the user to enter teir first name and en display the
#length of their name.
name = input ("Enter your first name ")
print (len(name))

#C021 
#Ask the user to enter their first name and then ask them to
#enter their surname. Join them together with a space between
#and display the name and the length of whole name.
firstname = input ("Enter your first name ")
surname = input ("Enter your surname ")
print (firstname, surname, len(firstname + surname))

#C22
#Ask the user to enter their first name and surname in lower
#case. Change the case to title case and join them together.
#Display the finished result.
firstname = str.lower( input ("Enter your first name "))
surname =  str.lower (input ("Enter your surname "))
tfirstname = firstname.title ()
tsurname = surname.title ()
print (tfirstname + " " + tsurname)

#C23
#Ask the user to type in the first line of a nursery rhyme and
#display the length of the string. Ask for a starting number and an
#ending number and then display just that section of the text
#(remember Python starts counting from 0 and not 1).
firstline = input ("Enter a first line of a nursery rhyme ")
startnum = int (input ("Choose a starting number: "))
endnum = int (input ("Choose a ending a number: "))
print (len (firstline))
print (firstline [startnum - 1: endnum - 1])

#C24
#Ask the user to type in any word and display it in upper case.
word = input ("Enter the first thing that comes to you r mind: ")
print (word.upper())

#C25
#Ask the user to enter their first name. If the length of their first name is under five characters, ask
#them to enter their surname and join them together (without a space) and display the name
#in upper case. If the length of the first name is five or more characters, display their first name in
#lower case.
firstname = input ("Enter your first name: ")
lenname = len (firstname)
if lenname < 5:
    surname = input ("Enter yout surname: ")
    name = firstname + surname
    print (name.upper ())
else:
    print (firstname.lower ())

#C26
#Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an
#“ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay,
#banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the
#user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case.
print ("Hi! Lets play Pig Latin!")
word = input ("Enter a word: ")
lenword = len (word)
firstword = word [0]
restword = word [1:lenword]
if firstword !="a" and firstword !="e" and firstword !="i" and firstword !="o" and firstword !="u":
    print (restword + firstword)
else:
    print (word + way)