#Sum of digits in n using recursive method
sum=0
def sum_of_digits(n):
  if n<10:
    return n
  return (n%10) + (sum_of_digits(n//10)) 

n=int(input("Enter n:"))
print(sum_of_digits(n))
   
#Constraints:
#Time complexity:O(logn)
#Auxilary Space:O(logn)