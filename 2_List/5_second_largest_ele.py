# Second Largest Element in a List
def second_largest_ele(l):
  lar=l[0]
  slar=None
  for i in range(1,len(l)):
    if l[i]>lar:
      slar=lar
      lar=l[i]
    elif l[i]<lar:
      if slar==None or l[i]>slar :
        slar=l[i]
  return slar

l=[10,10,10]
print(second_largest_ele(l))


#Constraints:
#Time Complexity:theta(n)
#Space complexity:O(1)
#Auxilary Space:O(1)
