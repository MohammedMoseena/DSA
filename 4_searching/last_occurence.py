#Index of last Occurrence
def last_occurrence(arr,x):
  high=len(arr)-1
  low=0
  while low<=high:
    mid=(high-low)//2 + low
    if arr[mid]>x:
      high=mid-1
    elif arr[mid]<x:
      low=mid+1
    elif (mid==(len(arr)-1)) or (arr[mid]!=arr[mid+1]):
      return mid
    else:
      low=mid+1
  return -1

arr=[8,10,10,12]
x=7
print(last_occurrence(arr,x))

#Constraints:
#Time complexity:O(logn)
#Space complexity:O(1)
