# Insertion Sort using Binary search

def binary_search(arr,temp,low,high):
  while low<=high:
    mid=(high-low)//2+low
    if arr[mid]==temp:
      return mid+1
    elif arr[mid]>temp:
      high=mid-1
    elif arr[mid]<temp:
      low=mid+1
  return low
def insertion_sort(arr,n):
  for i in range(1,n):
    temp=arr[i]
    if arr[i-1]>temp:
      pos=binary_search(arr,temp,0,i-1)
      arr=arr[0:pos]+[temp]+arr[pos:i]+arr[i+1:]
  return arr

arr=[10,9,8,7,6,5,4,3,2,1]
print(insertion_sort(arr,len(arr)))


#Best case: Sorted :O(n)
#Worst case: Reverse sorted: O(n^2)


#Constraints:
#Time complexity: O(n^2) : Even we are using binary search insertion takes O(n) time
#Auxilary space:O(1)
