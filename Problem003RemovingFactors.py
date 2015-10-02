#!/usr/bin/env python

#Project Euler Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?
#
#Script written by Cory Haight-Nali on or around 08 September 2015
#Basically an implementation of code found at https://stackoverflow.com/questions/12605320/project-euler-3-why-does-this-method-work

import math

n = 600851475143 #int(raw_input("Input # to find the largest prime factor of \n"))
for i in range(2, 1000000):
	while(n % i == 0):
		n //= i
		if(n == 1):
			print i, "is the largest factor"
			break


raw_input("Press any key to exit")
