#!/usr/bin/env python

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
#
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#
#Written by Cory Haight-Nali on or around 06 August 2015

#Brute force it !  Set c to a large number, keep a + b + c = 1000, and iterate
#through testing all combinations
for c in xrange(999, 0, -1):
    for b in xrange(999 - c, 0, -1):
        a = 1000 - c - b
        if(a**2 + b**2 == c**2):
            print "a = ", a, " b = ", b, " and c = ", c
            print "The product abc = ", a * b * c
            raw_input("Press any key to exit")
            break

    



