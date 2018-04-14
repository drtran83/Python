# Write a Python program that asks for a duration of time in hours and minutes
# and writes that the total duration only in minutes.

# Written by Tom Tran
# Date: March 28, 2018
# Class:  CIS 176 - Introduction to Computer Science
# Week: 4
# Assignment: Dropbox 4 - Question 6.

print ("This is Tom's Hours to minutes calculator")

# ask user for the hours

hours = int(input("\nEnter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))

# calculations: 
minutesPerHour = hours * 60

totalMinutes = minutesPerHour + minutes

#output

print("The total number of minutes is: ", totalMinutes)
