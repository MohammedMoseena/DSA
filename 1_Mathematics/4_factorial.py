# calculate the factorial of a number using both recursive and iterative method

#Note: Iterative Approach is best algorithm than Recursive Approach  even though both methods have same time complexity because it has constant auxilary space

# Recursive Approach
def factorial(n):
  if n<=0:
    print("Invalid number")
  elif (n==0 or n==1):
    return 1
  else:
    return n*factorial(n-1)

n=int(input("Enter n(recursive approach):"))
print(f"Factorial of n using recursive method:{factorial(n)}")

#Constraints
#Time complexity: theta(n)
#Space complexity:theta(1)
#Auxilary space:theta(n)

#Iterative approach
def iter_factorial(n):
  if (n==0 or n==1):
    return 1
  else:
    res=1
    for i in range(2,n+1):
      res=res*i
    return res
  
n=int(input("Enter n(iterative approach):"))
print(f"Factorial of n using iterative method:{factorial(n)}")

#Constraints
#Time complexity:theta(n)
#Space complexity:theta(1)
#Auxilary Space:theta(1)
  

