# To get floor of log of n
def log_n(n):
  if n==1:
    return 0
  return 1+ log_n(n//2)

n=int(input("Enter n:"))
print(log_n(n))

#Constraints:
#Time complexity: O(logn)
#Auxilary Space:O(logn)