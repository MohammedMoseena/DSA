# Index of First Occurence 
def first_occurence(arr,x):
  low=0
  high=len(arr)-1
  while low<=high:
    mid=(high-low)//2 + low
    if arr[mid]>x:
      high=mid-1
    elif arr[mid]<x:
      low=mid+1
    elif (mid==0) or (arr[mid]!=arr[mid-1]):
      return mid
    else:
      high=mid-1 
  return -1

arr=[15,15,15]
x=15
print(first_occurence(arr,x))

#Constraints:
#Time complexity:O(logn)
#Space complexity:O(1)




