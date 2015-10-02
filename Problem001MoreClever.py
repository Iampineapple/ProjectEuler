#!/usr/bin/env python

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.


total = 0

#Add multiples of 3 less than 1k
total = 3 * (333*(334))/2.0

#Add multiples of 5 less than 1k
total += 5 * (199*(200))/2.0

#Subtract multiples of 15 less than 1k, as we've now added them twice
total -= 15 * (66*(67))/2.0

print "The total is", total
raw_input("Press any key to exit")