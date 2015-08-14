#!/usr/bin/env python
# -*- coding: cp1252 -*-

#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#How many such routes are there through a 20×20 grid?
#
#Written by Cory Haight-Nali on or around 07 August 2015


#You take 40 steps.  WLOG, 20 of them are down.
#Thus, we're just calculating the ways to choose which 20 of the 40 are down.
#Aka 40 choose 20.
from math import factorial
print "From the top left to bottom right of a 20 by 20 grid,"
print "there are ", factorial(40) / (factorial(20) ** 2), " paths."
raw_input("Press any key to exit.")
