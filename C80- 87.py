# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 15:45:57 2022

@author: Risse
"""

#080
#Ask the user to enter their first name and then display
#the length of their first name. Then ask for their surname
#and display the length of their surname. Join their first
##name and surname together with a space between and
#display the result. Finally, display the length of their full name 
#(including the space)
firstname = input ("Enter your first name: ")
len_fn = len(firstname)
print (len_fn)
surname = input ("Enter your last name: ")
len_un = len(surname)
print (len_un)
fullname = firstname + " " + surname
print(fullname)
print (len(fullname))

#081
#Ask the user to type in their favourite school subject.
#Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.
subject = input ("Enter your favorite subject: ")
for letter in subject:
    print (letter, end = "-")
    
#082
#Show the user a line of text from your favourite poem
#and ask for a starting and ending point. Display the
#characters between those two points.    
poem ="'Tis better to have loved and lost than never to have loved at all"
print (poem)
start = int (input ("Enter the starting number: "))
end = int (input ("Enter the ending number: "))    
print (poem [start:end])   
    
#083
#Ask the user to type in a word in upper case. If they
#type it in lower case, ask them to try again. Keep
#repeating this until they type in a message all in uppercase.
word = input ("Type a word in uppercase: ") 
while word.islower ():
    word = input ("Type a word in uppercase: ") 
    
#084
#Ask the user to type in their postcode. Display the first
#two letters in uppercase.   
postcode = input ("Enter your postcode: ")
print (postcode[0:2].upper())   
    
    
#085
#Ask the user to type in their name and then tell them how many vowels are 
#in their name.    
name = input ("Enter your name: ")
name = name.lower()
vowels = 0;
for letter in name:
    if letter == "a" :
        vowels = vowels + 1;        
    if letter == "e" :
        vowels = vowels + 1;  
    if letter == "i" :
        vowels = vowels + 1;     
    if letter == "o" :
        vowels = vowels + 1;     
    if letter == "u" :
        vowels = vowels + 1;     
print ("There are", vowels, "vowels in your name.")    
    
name = input ("Enter your name: ")
name = name.lower()
vowels = 0;
for letter in name:
    if letter == "a"  or letter == "e"  or letter == "i"  or letter == "o"  or letter == "u"  :
        vowels = vowels + 1;           
print ("There are", vowels, "vowels in your name.")        
    
#086
#Ask the user to enter a new password. Ask them to enter it again. If the two passwords
#match, display “Thank you”. If the letters are correct but in the wrong case, display the
#message “They must be in the same case”, otherwise display the message “Incorrect”.
password1 = input ("Enter new password: ")
password2 = input ("Enter the password again: ")
if password1 == password2:
    print ("Thank You.")
elif password1.lower() == password2.lower():
    print ("They must be in the same case.")
else:
    print ("Incorrect.")


#087
#Ask the user to type in a word and then display it backwards on separate lines. For
#instance, if they type in “Hello” it should display as shown below:
word = input ("Enter a word: ")
lenword = len (word)
for letter in word:
    print (word[lenword-1])
    lenword = lenword - 1
    


    
    
    
    