#!/usr/bin/env python

#Project Euler Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#Program does this by brute force checking each number below 1000, 
#and adding it to the total if it is divisible by 3 or 5


total = 0 #The sum of all numbers in question
belowNumber = 1000 #The max number we're looking at


#Add up all the multiples of 3
for current in range(3, belowNumber, 3):
    total += current

#Reset current number, add up all multiples of 5 that aren't multiples of 3

for current in range(5, belowNumber, 5):
    if current % 3 != 0: 
        total += current

print total
raw_input("Press enter to exit")
