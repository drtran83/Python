# This program will get the length and width of a rectangle from the user and
# will compute and print the area.
#
# Written by Tom Tran
# Date: March 27, 2018
# Class:  CIS 176 - Introduction to Computer Science
# Week: 4
# Assignment: Dropbox 4 - Question 1.

print ('This is Tom Trans Rectangle Area Calculator')

#Get user input
length = input ('\nEnter the length of the rectangle: ')
width = input ('Enter the width of the rectangle: ')

length = int (length)
width = int (width)

#calculate
area = length*width

print ('\nThe area of the rectangle is: ', area) 

input ("\n\nPress the Enter key to exit")


