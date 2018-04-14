# Write a Python program that asks for the user's age in years and policy amount.
# if the user is under 35, then quote an insurance rate of 2.23 per $100
# for life insurance, otherwise quote a rate of $4.32

# Written by Tom Tran
# Date: March 28, 2018
# Class:  CIS 176 - Introduction to Computer Science
# Week: 4
# Assignment: Dropbox 4 - Question 7.

# Welcome message

print ("Welcome to Tom's insurance rate calcuator")

#get age from user
age = int(input("\nPlease enter your age: "))
policyAmount = int(input("Pleae enter the policy amount $"))

# if age is less than 35 calculate the rate and print
if age < 35:
    insuranceRate = 2.23 / 100
    totalRate = insuranceRate * policyAmount
    print ("Your Insurance Rate is $ " , totalRate)

#else when age is greater than 35 calculate the rate and print

else:
    insuranceRate = 4.32 / 100
    totalRate = insuranceRate * policyAmount
    print ("Your Insurance Rate is $" , totalRate)



    
