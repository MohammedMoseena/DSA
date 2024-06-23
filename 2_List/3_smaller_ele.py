# Get Smaller Elements
def smaller_elements(l,x):
  # res=[]
  # for i in range(0,len(l)):
  #   if l[i]<x:
  #     res.append(l[i])
  # Using List comprehension
  #List comprehension helps us to reduce lines of code
  return [l[i] for i in range(len(l)) if l[i]<x]

l=[8,100,20,40,3,7]
x=10
print(smaller_elements(l,x))

#Time complexity:O(n)
#Space complexity:O(n)
#Auxilary Space:O(1)