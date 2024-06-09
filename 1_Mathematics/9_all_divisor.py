# All divisors of a number
'''
Efficient Method Approach:
1. Observation: Divisors of a number exist in pairs, where one divisor is less than or equal to the square root of the number, and the other divisor is greater than the square root.
2. Divisor Pairs: For any pair (x, y) where x * y = num, either x or y is less than or equal to the square root of num.
3. Efficient Traversal: Instead of traversing from 1 to num to find divisors, it's sufficient to traverse from 1 to square root of num. This reduces the time complexity significantly.
'''
def divisors(num):
  i=1
  while i*i<num:
    if num%i==0:
      print(i,end=" ")
    i+=1
  while i>=1:
    if num%i==0:
      print(num//i,end=" ")
    i-=1
    
num=int(input("Enter the number:"))
divisors(num)

#Constraints:
# Time complexity:O(n^0.5)
# Space complexity:O(1)
# Auxilary Space: O(1)