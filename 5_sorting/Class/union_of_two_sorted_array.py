#Union of two sorted arrays
def union_of_two_sorted_arrays(a,b):
  i=0
  j=0
  while i<len(a) and j<len(b):
    if (i>0 and a[i]==a[i-1]):
      i+=1
    elif (j>0 and b[j]==b[j-1]):
      j+=1
    elif (a[i]<b[j]):
      print(a[i],end=" ")
      i+=1
    elif (b[j]<a[i]):
      print(b[j],end=" ")
      j+=1
    elif(a[i]==b[j]):
      print(a[i],end=" ")
      i+=1
      j+=1
  while i<len(a) :
    if (a[i]!=a[i-1]):
      print(a[i],end=" ")
    i+=1
  while j<len(b) :
    if (b[j]!=b[j-1]):
      print(b[j],end=" ")
    j+=1

a=[3,5,8]
b=[2,8,9,10,15]
union_of_two_sorted_arrays(a,b)
    
#Constraints:
#Time complexity:theta(m+n)
#Auxilar space:O(1)
