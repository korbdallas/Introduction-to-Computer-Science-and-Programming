
# Problem Set 0
# Name: Michael Colombo
# Collaborators:
# Time:
#

# A Very Simple Program: Entering and Printing Your Name
# The goal of this programming exercise is simply to get you more comfortable with using IDLE,
# and to begin using simple elements of Python. Standard elements of a program include the
# ability to print out results (using the print operation), the ability to read input from a user at the
# console (for example using the raw_input operation), and the ability to store values in a
# variable, so that the program can access that value as needed.
# Problem 1.
# Write a program that does the following in order:
# 1. Asks the user to enter his/her last name.
# 2. Asks the user to enter his/her first name.
# 3. Prints out the user’s first and last names in that order

#!/usr/bin/env python

LastName=input("What is your last name? ") # Gather last name
FirstName=input("What is your first name? ") # gather first name

print (FirstName + " " + LastName) # print names in expected order
