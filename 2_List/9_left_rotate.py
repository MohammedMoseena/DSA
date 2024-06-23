# Left Rotate a list by one
def left_rotate(l):
  temp=l[0]
  for i in range(1,len(l)):
    l[i-1]=l[i]
  l[-1]=temp
  return l


l=[1,2,3,4,5]
print(left_rotate(l))

#Time complexity:O(n)
#Auxilary Space:O(1)