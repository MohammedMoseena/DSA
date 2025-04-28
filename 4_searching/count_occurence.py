# Cout of occurrences in a sorted array
# count of occurrence in a sorted array is equal to (last_occurence-first_occ+1)

def first_occurence(arr,x):
  low=0
  high=len(arr)-1
  while low<=high:
    mid=(high-low)//2+low
    if arr[mid]>x:
      high=mid-1
    elif arr[mid]<x:
      low=mid+1
    elif mid==0 or arr[mid]!=arr[mid-1]:
      return mid
    else:
      high=mid-1
  return -1

def last_occurence(arr,x):
  low=0
  high=len(arr)-1
  while low<=high:
    mid=(high-low)//2+low
    if arr[mid]>x:
      high=mid-1
    elif arr[mid]<x:
      low=mid+1
    elif mid==(len(arr)-1) or arr[mid]!=arr[mid+1]:
      return mid
    else:
      low=mid+1
  return -1

def count_of_occurence(arr,x):
  first=first_occurence(arr,x)
  if first==-1:
    return 0
  last=last_occurence(arr,x)
  return last-first+1

arr=[10,20,20,20,30,30]
x=20
print(count_of_occurence(arr,x))


#Constraints
#Time complexity:O(logn)
#Auxilary space:O(1)
