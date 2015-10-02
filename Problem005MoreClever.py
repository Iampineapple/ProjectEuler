#!/usr/bin/env python

#Project Euler Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Split the numbers into prime factorization by hand, then multiply the largest
#power of any prime together
print  2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
