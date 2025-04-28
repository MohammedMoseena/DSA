# Recursive binary search
def recursive_binary_search(arr,x,low,high):
  if low>high:
    return -1
  mid=(high-low)//2 + low
  if arr[mid]==x:
    return mid
  elif arr[mid]>x:
    return recursive_binary_search(arr,x,low,mid-1)
  else:
    return recursive_binary_search(arr,x,mid+1,high)
arr=[10,20,30,40,50,60,70]
x=20
low=0
high=len(arr)-1
print(recursive_binary_search(arr,x,low,high))

#Constraints:
#Time complexity:O(logn)
#Auxilary Space:O(logn)



  
