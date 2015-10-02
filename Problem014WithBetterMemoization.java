/*
 * #Project Euler Problem 14:
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
#This script was translated from python by Cory Haight-Nali on or around 17 September 2015

 */

package projectEuler;

public class Problem014WithBetterMemoization {
	
	//Takes in a long n, and the memolist, and returns the length
	//of the collatz sequence starting with n
	//Using Java's pass-by-reference-for-data-structures thing to modify memolist in place
	public static int CollatzLength(long n, int[] memolist){
		if(n < memolist.length && memolist[(int)n] != 0){
			return memolist[(int)n];
		}//if it's already memoized
		if(n == 1){
			memolist[1] = 1;
			return 1;
		}//if base case
		if(n % 2 == 0){
			int length = CollatzLength(n/2, memolist);
			if(n < memolist.length){
				memolist[(int)n] = length + 1;
			}
			return length + 1;
		}//if n is even
		else{
			int length = CollatzLength(3*n + 1, memolist);
			if(n < memolist.length){
				memolist[(int)n] = length + 1;
			}
			return length + 1;
		}//if n is odd
	}//CollatzLength
	
	public static void main(String[] args){
		//initialization of variables we'll need
		int[] memolist = new int[1000001];
		long longestNum = 1;
		int longestLength = 1;
		int length;
		
		//Using the memoized method, check all Collatz sequence lengths
		for(int i = 1; i <= 1000000; i++){
			length = CollatzLength(i, memolist);
			if(length > longestLength){
				longestLength = length;
				longestNum = i;
			}//check if i starts the longest sequence
		}//for to find the longest
		
		System.out.print("The longest sequence with a starting number ");
		System.out.print("less than 1 million \n began with " + longestNum);
		System.out.print(" which started a sequence of " + longestLength + " numbers.");
		
	}
	
}
