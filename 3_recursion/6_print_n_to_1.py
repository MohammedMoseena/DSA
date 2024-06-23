#Print n to 1 using recursive function
def print_n(n):
  if n==0:
    return
  print(n)
  print_n(n-1)

n=int(input("Enter n:"))
print_n(n)
#Constraints:
#Time complexity:O(n)
#Auxilary Space:O(n)