# Write a Python program that reads in 10 integer quiz grades and computes
# the average grade

# Written by Tom Tran
# Date: March 28, 2018
# Class:  CIS 176 - Introduction to Computer Science
# Week: 4
# Assignment: Dropbox 4 - Question 8.

# Welcome message

print ("Welcome to Tom's grade calculator")

#get grades from user

grade1 = int(input("\nEnter the first quiz grade: "))
grade2 = int(input("Enter the second quiz grade: "))
grade3 = int(input("Enter the third quiz grade: "))
grade4 = int(input("Enter the fourth quiz grade: "))
grade5 = int(input("Enter the fifth quiz grade: "))
grade6 = int(input("Enter the sixth quiz grade: "))
grade7 = int(input("Enter the seventh quiz grade: "))
grade8 = int(input("Enter the eigth quiz grade: "))
grade9 = int(input("Enter the ninth quiz grade: "))
grade10 = int(input("Enter the tenth quiz grade: "))

#calculate

totalGradeScore = grade1+grade2+grade3+grade4+grade5+grade6+grade7+grade8+grade9+grade10

average = totalGradeScore/10

#output
print ("The average of the 10 grades is: ", average)

