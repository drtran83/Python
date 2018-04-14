# This program will get a single character from the user and will write out
# a congratulatory message if the character is a vowel (a, e, i, o, u)
# but other wise writes out "You lose, better luck next time" message.

# Written by Tom Tran
# Date: March 27, 2018
# Class:  CIS 176 - Introduction to Computer Science
# Week: 4
# Assignment: Dropbox 4 - Question 2.

print ("Welcome to Tom's Letter Game\n")

#Get user input

charInput = str(input ("Enter any letter of the alphabet and let's see if you win!: "))

#if/else statement

if charInput in 'aeiouy':
    print ("\nCongratulations you've won!")

else: print("\nSorry! You lose, better luck next time!")


input ("\n\nPress the Enter key to exit")


