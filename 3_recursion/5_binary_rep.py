#Binary represention of n using recursive function
def binary_rep(n):
  if n==0:
    return
  binary_rep(n//2)
  print(n%2,end="")

n=int(input("Enter n:"))
binary_rep(n)
  
#Constraints:
#Time complexity:O(logn)
#Auxilary Space:O(logn)