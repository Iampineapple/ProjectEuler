#!/usr/bin/env python

#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 2^1000?
#
#Written by Cory Haight-Nali on or around 07 August 2015


mystring = str(2**1000)
total = 0
for i in range(0, len(mystring), 1):
    print int(mystring[i])
    total += int(mystring[i])

print "The total is ", total
raw_input("Press any key to exit.")
