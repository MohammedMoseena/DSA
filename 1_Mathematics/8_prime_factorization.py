# This code performs prime factorization of a given number using the Sieve of Eratosthenes method.
'''
Approach:

1. Initialize a boolean list isPrime of size num+1, where each element represents whether the corresponding index is prime or not.
2. Loop through all numbers from 2 to num.
3. For each prime number i, mark all multiples of i as non-prime in the isPrime list.
3. While marking multiples, also perform prime factorization for num by dividing it by i until it's no longer divisible by i.
4. Continue this process until all numbers up to num are processed.


'''

def PrimeFactorization(num):
    # Initialize variables
    i = 2
    isPrime = [True] * (num + 1)  # Initialize a boolean list to mark prime numbers
    # Loop through all numbers from 2 to num
    while i <= num:
        if isPrime[i]:  # Check if i is marked as prime
            temp = num  # Initialize a temporary variable to store num
            # Print i as a prime factor and update temp
            while temp % i == 0:
                print(i, end=" ")
                temp = temp // i
            # Mark multiples of i as non-prime
            for j in range(i * i, num + 1, i):
                isPrime[j] = False
        i += 1

# Take an integer input from the user.
num = int(input("Enter num:"))

# Perform prime factorization of the input number.
PrimeFactorization(num)

#Constraints:
#Time complexity:O(nlogn)
#Space complexity:O(n)
#Auxilary Space:O(1)