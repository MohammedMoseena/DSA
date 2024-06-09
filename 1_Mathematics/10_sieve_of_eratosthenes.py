# prints all prime numbers up to a given number using the Sieve of Eratosthenes algorithm.

'''
Sieve of Eratosthenes Algorithm:
1. Initialization: Create a boolean list (isPrime) of size num+1, where each element represents whether the corresponding index is prime or not. Initially, all numbers are marked as prime.
2. Main Loop: Starting from 2, iterate through each number up to num.
3. Prime Marking: For each prime number i, mark all multiples of i as non-prime in the isPrime list. Start marking from i*i (because any smaller multiple of i would already be marked by a smaller prime).
4. Printing: Print the prime numbers (those for which isPrime[i] is True).
5. Efficiency: By the end of the loop, isPrime will contain True only for prime numbers.
'''
def all_primes(num):
  isPrime=[True]*(num+1)
  i=2
  while i<=num:
    if isPrime[i]:
      print(i,end=" ")
      for j in range(i*i,num+1,i):
        isPrime[j]=False
    i+=1
num=int(input("Enter the number:"))
all_primes(num)

#Time complexity:O(nloglogn)
#Space complexity:O(n)
#Auxilary Space:O(1)