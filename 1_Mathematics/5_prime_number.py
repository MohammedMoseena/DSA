'''
Approach:

1. Input: Read an integer input from the user.

2. Special Cases:
  a. If n is 1, return False because 1 is not a prime number.
  b. If n is 2 or 3, return True because both 2 and 3 are prime numbers.
  c. If n is divisible by 2 or 3, return False as it cannot be prime (excluding multiples of 2 and 3 early).
3. Prime Check Loop:
  a. Initialize i to 5.
  b. Use a while loop to check for factors from i to the square root of n:
     If n is divisible by i or i + 2, return False (checking divisibility by i and i+2 covers numbers of the form 6k ± 1).
  c. Increment i by 6 to skip checking multiples of 2 and 3 (i.e., numbers of the form 6k ± 1 are potential primes).
4. Result: If no factors are found in the loop, return True indicating that n is a prime number.

Q1. Why Loop Until Square Root of n:
Any non-prime number n must have at least one factor less than or equal to √n. Therefore, if n is not divisible by any number up to √n, it is a prime number. This significantly reduces the number of checks needed compared to checking up to n.

Q2. Why i=5 and i+=6:
After checking for divisibility by 2 and 3, we skip checking numbers that are multiples of 2 or 3.
Numbers that are not multiples of 2 or 3 can be expressed as 6k ± 1 (i.e., numbers like 5, 7, 11, 13, etc.). By incrementing i by 6 each time and checking i and i + 2, we efficiently test only the relevant potential factors, thus optimizing the prime-checking process.

'''

def isprimenumber(n):
  if n==1:
    return False
  if n==2 or n==3:
    return True
  if n%2==0 or n%3==0:
    return False
  i=5
  while i*i<=n:
    if n%i==0 or n%(i+2)==0:
      return False
    i+=6
  return True

n=int(input("Enter n:"))
print('true') if isprimenumber(n) else print('false')

# Constraints
# Time complexity: O(n^0.5)
# Space complexity: O(1)
# Auxilary Space: O(1)

  

