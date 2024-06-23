#Factorial of  a number using recursive method

def fact(n):
  if n<0:
    return None
  if n==0:
    return 1
  return n*fact(n-1)

n=0
print(fact(n))