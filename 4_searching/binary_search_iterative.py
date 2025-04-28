# Binary search is used to search element in sorted array 
# To search an element in an array using naive approach it takes O(n) time complexity
# To search an element in an sorted array using binary search takes O(logn) time complexity

def binary_search(arr,x,n):
  low=0
  high=n-1
  while low<=high:
    mid=(high-low)//2 + low
    if x==arr[mid]:
      return mid
    if x<arr[mid]:
      high=mid-1
    if x>arr[mid]:
      low=mid+1
  return -1

arr=[10,10]
x=10
n=len(arr)
print(binary_search(arr,x,n))

#Constraints:
#Time complexity:O(logn)
#Auxilary Space:O(1)


