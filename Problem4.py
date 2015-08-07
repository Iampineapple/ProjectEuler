#!/usr/bin/env python

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.
#
#This script was written by Cory Haight-Nali on or around 01 August 2015

#Function to take number, and extract the digit number digit from it, 
#counting from the right
def digitExtractor(number, digit):
	key = 10**(digit - 1)
	ext = number/key
	ext = ext % 10
	return ext

#Function to take a number, and check if it is palindromic
#By the problem constraints, isPalindromic only checks up to 6 digit numbers
def isPalindromic(number):
        #First find the largest digit in the number
        maxDigit = 6
        while(digitExtractor(number, maxDigit) == 0):
                maxDigit -= 1

        #Next, test for palindromicness
        palindromic = True
        i = 1
        while(maxDigit + 1 - i > i):
              if(digitExtractor(number, maxDigit + 1 - i) != digitExtractor(number, i)):
                      palindromic = False
                      break
              i += 1
        return palindromic

#Brute force to find largest palindromic number
largestPalindrome = 1
for i in range(100, 1000, 1):
        for j in range(100, 1000, 1):
                if(isPalindromic(i * j) and largestPalindrome < i * j):
                        largestPalindrome = i * j

print "The largest palindrome was ", largestPalindrome
raw_input("Press any key to exit")

        
