#!/usr/bin/env python

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.
#
#Written by Cory Haight-Nali on or around 06 August 2015

#Implement a sieve of Erastones which returns a list of primes
def sieveOfErastones(maxNum):
    from math import sqrt
    primeList = [2]
    for n in range(3, maxNum, 1):
        i = 0
        nPrime = True
        while(i < len(primeList) and primeList[i] <= sqrt(n)):
            if(n % primeList[i] == 0):
                nPrime = False
                break
            i += 1
        if(nPrime == True):
                    primeList.append(n)
    return primeList

#Get a list of all the primes less than 2 million
primeList = sieveOfErastones(2000000)

print "The total of all the primes is ", sum(primeList)
raw_input("Press any key to exit")
