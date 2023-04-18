
#Problem Set #0

#Problem 1
#Write a program that does the following in order:
#Asks the user to enter his/her date of birth.
#Asks the user to enter his/her last name.
#Prints out the user’s last name and date of birth, in that order.
#An example of an interaction with your program is shown below (the words printed in blue are from the
#computer, based on your commands, the words in black are a user’s input – the colors are simply here to
#help you distinguish the two components):
#
#Enter your date of birth:
#**01/26/32
#Enter your last name:
#**Grimson
#Grimson 01/26/32

# Problem Set 0
# Name: Michael Colombo 
# Collaborators:
# Time Spent:


#!/usr/bin/env python

birthday=input("Enter your date of birth in mm/dd/yy format: \n")
lastname=input("Enter your last name: \n")

print(lastname + " " + birthday)
