#Intersection of two sorted arrays

def intersection_of_two_sorted_arrays(a,b):
  i=0
  j=0
  while i<len(a) and j<len(b):
    if (i>0 and a[i]==a[i-1]):
      i+=1
    elif (j>0 and b[j]==b[j-1]):
      j+=1
    elif a[i]==b[j]:
      print(a[i],end=" ")
      i+=1
      j+=1
    elif a[i]<b[j]:
      i+=1
    elif a[i]>b[j]:
      j+=1

a=[1,1,3,3,3]
b=[1,1,1,1,3,5,7]
intersection_of_two_sorted_arrays(a,b)

#Constraint
#Time complexity:O(m+n)
#Auxilary space:O(1)