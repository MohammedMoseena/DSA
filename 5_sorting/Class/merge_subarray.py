#Merge Subarrays
#low to  mid is sorted
# mid+1 to high is
def merge_subarray(arr,low,mid,high):
  left=arr[low:mid+1]
  right=arr[mid+1:high+1]
  i=0
  j=0
  k=0

  while i<len(left) and j<len(right):
    if left[i]<=right[j]:
      arr[k]=left[i]
      i+=1
      k+=1
    else:
      arr[k]=right[j]
      j+=1
      k+=1
  while i<len(left):
    arr[k]=left[i]
    i+=1
    k+=1
  while j<len(right):
    arr[k]=right[j]
    j+=1
    k+=1
  return arr

arr=[10,15,20,11,13]
low=0
high=len(arr)-1
mid=(high-low)//2 + low
print(merge_subarray(arr,low,mid,high))

#Constraints:
#Time complexity:O(n)
#Auxilary space:O(n)