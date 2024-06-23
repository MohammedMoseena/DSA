#Print 1 to n using recursive function
def print_rec(n):
  if n==0:
    return
  print_rec(n-1)
  print(n)

n=int(input("Enter n:"))
print(print_rec(n))

#Constraints:
#Time complexity:O(n)
#Auxilary Space:O(n)