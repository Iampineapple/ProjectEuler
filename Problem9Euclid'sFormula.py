#!/usr/bin/env python

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a**2 + b**2 = c**2
#
#For example, 3**2 + 4**2 = 9 + 16 = 2**5 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#
#Written by Cory Haight-Nali on or around 06 August 2015,
#with some help from http://www.mathblog.dk/pythagorean-triplets/

#Definition of gcd, using Euclid's algorithm
def gcd(a, b):
    while(b != 0):
        (a, b) = (b, a % b)
    return a


#Euclid's formula, for c up to 1000
for m in xrange(2, 1001, 1):
    if(500 % m == 0):#Ensure we have a proper m
        if(m % 2 == 0):#Ensure that k is odd
            k = m + 1
        else:
            k = m + 2
        while(k < 2*m and k <= 1000/(2*m)):
            if(1000/(2*m) % k == 0 and gcd(k, m) == 1):
                d = 500 / (k * m)
                n = k - m
                a = d*(m*m - n*n)
                b = 2*d*m*n
                c = d*(m*m + n*n)
                print "a = ", a, " b = ", b, " and c = ", c
                print "The product abc = ", a * b * c
                raw_input("Press any key to exit")
                break
            k += 2

