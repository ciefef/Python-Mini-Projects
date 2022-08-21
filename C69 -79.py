# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 20:59:22 2022

@author: Risse
"""

#69
#Create a tuple containing the names of five countries and display the whole tuple. Ask
#the user to enter one of the countries that have been shown to them and then display
#the index number (i.e. position in the list) of that item in the tuple.
countries = ("Philippines", "Korea", "Japan", "Australlia", "Canada")
print (countries)
user = input ("Enter the country you've remembered: ")
print (countries.index(user))


#70
#Add to program 069 to ask the user to enter a number and
#display the country in that position.
countries = ("Philippines", "Korea", "Japan", "Australlia", "Canada")
print (countries)
#user = input ("Enter the country you've remembered: ")
print (countries.index(user))
num = int(input("Enter a number from 0 to 4: "))
print (countries[num])

#71
#Create a list of two sports. Ask the user what their favourite sport is and
#add this to the end of the list. Sort the list and display it.
sports = ["soccer", "basketball"]
user = input ("Enter your favorite sports: ")
sports.append (user)
sports.sort ()
print (sports)

#072
#Create a list of six school subjects. Ask the user which of these
#subjects they don’t like. Delete the subject they have chosen from the
#list before you display the list again.
subjects = ["math", "science", "AP", "mapeh", "english", "biology"]
print (subjects)
user = input ("Which subject you don't like the most? ")
subjects.remove (user)
print (subjects)
              
#073
#Ask the user to enter four of their favourite foods
#and store them in a dictionary so that they are
#indexed with numbers starting from 1. Display the dictionary in
#full, showing the index number and the item. Ask
#them which they want to get rid of and remove it
#from the list. Sort the remaining data and display
#the dictionary.
food_dictionary = {}
for i in range (0, 4):
    foods = input ("Enter your favorite foods: ")
    food_dictionary [i+1] = foods
print (food_dictionary)
dislike = int (input ("Which of these you dont like? "))
del food_dictionary [dislike]
print (sorted(food_dictionary))

#074
#Enter a list of ten colours. Ask the user for a starting
#number between 0 and 4 and an end number
#between 5 and 9. Display the list for those colours
#between the start and end numbers the user input.
colors = ["red", "green", "blue", "yellow", "purple", "orange", "white", "black", "brown", "sky blue"]
start_num = int (input ("Enter the starting number from 0 to 4: "))
end_num = int (input ("Enter end number from 5 to 9: "))
print (colors[start_num:end_num])

#075
#Create a list of four three-digit numbers. Display the list to the
#user, showing each item from the list on a separate line. Ask
#the user to enter a three-digitnumber. If the number they
# typed in matches one in the list, display the position of
#that number in the list, otherwise display the message “That is not in the list”.
num = [123, 456, 789, 987, 654]
for i in range (0, len(num)):
    print (num[i])
user = int (input ("Enter a three digit number: "))
if user in num:
    print (num.index(user))
else:
    print ("It's not in the list.")

#076
#Ask the user to enter the names of three people they want to
#invite to a party and store them in a list. After they have entered
#all three names, ask them if they want to add another. If they do,
#allow them to add more names until they answer “no”. When
#they answer “no”, display how many people they have invited to
#the party.
name = []
for i in range (0, 3):
    user = input ("Enter the name: ")
    name.append (user)
more = input ("Do you want to add more people? ")
while more == "yes":
    user = input ("Enter the name: ")
    name.append (user)
    more = input ("Do you want to add more people? ")
if more == "no":
    print ("You have invited", len(name), "people succesfully.")

#077
#Change program 076 so that once the user has completed their list of names, display the
#full list and ask them to type in one of the names on the list. Display the position of that
#name in the list. Ask the user if they still want that person to come to the party. If they
#answer “no”, delete that entry from the list and display the list again.
name = []
for i in range (0, 3):
    user = input ("Enter the name: ")
    name.append (user)
more = input ("Do you want to add more people? ")
while more == "yes":
    user = input ("Enter the name: ")
    name.append (user)
    more = input ("Do you want to add more people? ")
if more == "no":
    print ("You have invited", len(name), "people succesfully.")
print (name)
check = input ("Enter the name: ")
print (name.index(check))
want = input ("Do you want them to come to the party? ")
if want == "yes":
    print ("nice")
if want == "no":
    name.remove(check)
print (name)

#078
#Create a list containing the titles of four TV programmes and display
#them on separate lines. Ask the user to enter another show and a
#position they want it inserted into the list. Display the list again,
#showing all five TV programmes in their new positions.
tvshow = ["family feud", "eat bulaga", "showtime", "little forest"]
for i in range (0, len(tvshow)):
    print (tvshow[i])
user = input ("Enter another TV show: ")
num = int (input ("Where do you want to enter it? "))
tvshow.insert(num, user)
print (tvshow)

#079
#Create an empty list called “nums”. Ask the user to enter numbers.
#After each number is entered, add it to the end of the nums list and
#display the list. Once they have entered three numbers, ask them if
#they still want the last number they entered saved. If they say “no”,
#remove the last item from the list. Display the list of numbers.

nums = []
for i in range (0, 3):
    user = int (input ("Enter a number: "))
    nums.append (user)
check = input ("Do you still want the last number you entered? ")
if check == "yes":
    print ("nice")
if check == "no":
    nums.remove (nums[2])
print (nums)

