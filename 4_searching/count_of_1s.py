#Count of 1s in a sorted binary list
def first_occurence_1(arr,x):
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

def count_of_xs(arr,x):
  first=first_occurence_1(arr,x)
  if first==-1:
    return 0
  return len(arr)-first

arr=[1,1,1,1,1]
x=1
print(count_of_xs(arr,x))


