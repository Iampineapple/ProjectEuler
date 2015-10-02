#!/usr/bin/env python

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.
#
#This script was written by Cory Haight-Nali on or around 01 August 2015

#Function to take number, and extract the digit number digit from it, 
#counting from the right
#Nifty string slicing def of isPalindromic taken from http://code.jasonbhill.com/c/project-euler-problem-4/
#and improves runtime some
		
def isPalindromic(number):
	return (str(number) == (str(number)[::-1]))

#Brute force to find largest palindromic number
largestPalindrome = 1
for i in range(100, 1000, 1):
        for j in range(i + 1, 1000, 1):
                if(isPalindromic(i * j) and largestPalindrome < i * j):
                        largestPalindrome = i * j

print "The largest palindrome was ", largestPalindrome
raw_input("Press any key to exit")
