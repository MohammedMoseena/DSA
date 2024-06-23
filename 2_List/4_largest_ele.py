# Largest Element in a list
def large_ele(l):
  if len(l)==0:
    return None
  if len(l)==1:
    return l[0]
  max_val=l[0]
  for i in range(1,len(l)):
    if l[i]>max_val:
      max_val=l[i]
  return max_val

l=[40]
print(large_ele(l))

#Constraints:
#Time complexity: theta(n)
#Space complexity: O(1)
#Auxilary complexity: O(1)