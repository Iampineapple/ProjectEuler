#!/usr/bin/env python
# -*- coding: utf-8 -*-

#The following iterative sequence is defined for the set of positive integers:
#
#n ? n/2 (n is even)
#n ? 3n + 1 (n is odd)
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
#Otherwise, increment length, and recursively call CollatzLength
#on the next n
def CollatzLength(n, length, memolist):
    if(n < len(memolist) and memolist[n] != -1):
        length += memolist[n]-1
        return length
    if(n == 1):
        return length
    if(n%2 == 0):
        length = CollatzLength(n/2, length+1, memolist)
        return length
    else:
        length = CollatzLength(3*n+1, length+1, memolist)
        return length



memolist = [-1]*1000001
longestnum = 1
longestlength = 1
for i in xrange(1, 1000000, 1):
    length = CollatzLength(i, 1, memolist)
    memolist[i] = length
    if(length > longestlength):
        longestlength = length
        longestnum = i

print "The longest sequence less than 1 million started with", longestnum
raw_input("Press any key to exit")
