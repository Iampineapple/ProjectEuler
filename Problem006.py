#!/usr/bin/env python

#Project Euler Problem 6
#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 552 = 3025
#
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


#Initialize all counters as zero.  
#theNumber will be our iterator.  squareSum will be the sum of all squares.
#sumToSquare will sum up all numbers, then be squared as sumSquare.
squareSum = 0
sumToSquare = 0
sumSquare = 0

#Do the appropriate math, then increment theNumber.
for theNumber in range(0, 101, 1):
    squareSum += theNumber * theNumber
    sumToSquare += theNumber

#Make sure to square sumToSquare
sumSquare = sumToSquare * sumToSquare

#Print the difference
print "The difference between the sum of all squares of the first"
print "hundred natural numbers and the square of the sum of the same numbers"
print "is ", sumSquare - squareSum
raw_input("Press enter to exit")
