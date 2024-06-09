# Trailing Zeros in Factorial

'''
Trailing 0s in n! = Count of 5s in prime factors of n!
                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
'''
import math
# count trailing 0s
# in n !

# Function to return
# trailing 0s in
# factorial of n
def findTrailingZeros(n):
	
	# Initialize result
	count = 0

	# Keep dividing n by
	# powers of 5 and
	# update Count
	i = 5
	while i<=n:
		count += math.floor(n/i)
		i *= 5

	return count

# Driver program
n = 100
print("Count of trailing 0s "+
	"in 100 ! is", findTrailingZeros(n))

#Constraints:
#Time complexity:O(logn)
#Space complexity:O(1)
#Auxilary Space:O(1)


