#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Project Euler Problem 14:
#The following iterative sequence is defined for the set of positive integers:
#
#n = n/2 (n is even)
#n = 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#13 ? 40 ? 20 ? 10 ? 5 ? 16 ? 8 ? 4 ? 2 ? 1

#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.
#
#This script was written by Cory Haight-Nali on or around 14 August 2015

#Check if the length for a given n has already been computed.
#If so, add it to the current length total, return that up the recursion.
#Otherwise, recursively call CollatzLength on the next n, 
#get that length, increment it, save it, and return it
def CollatzLength(n, memolist):
    if(n < len(memolist) and memolist[n] != -1):
        length = memolist[n]
        return length, memolist
    if(n == 1):
        return 1, memolist
    if(n%2 == 0):
        length, memolist = CollatzLength(n/2, memolist)
        if(n < len(memolist)):
            memolist[n] = length + 1
        return length + 1, memolist
    else:
        length, memolist = CollatzLength(3*n+1, memolist)
        if(n < len(memolist)):
            memolist[n] = length + 1
        return length + 1, memolist


#Initialize the memolist with -1 as the magic unset value
#Set longest number and longest collatz length to 1, for the length(1)
memolist = [-1]*1000001
memolist[1] = 1
longestnum = 1
longestlength = 1

#Check the length of every number 1 to 1million, and find the longest
for i in xrange(1, 1000000, 1):
    length = CollatzLength(i, memolist)
    if(length > longestlength):
        longestlength = length
        longestnum = i

print "The longest sequence less than 1 million started with", longestnum
raw_input("Press any key to exit")
