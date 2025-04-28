def merge_subarray(arr,low,mid,high):
  left=arr[low:mid+1]
  right=arr[mid+1:high+1]
  i=0
  j=0
  k=low
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

def merge_sort(arr,low,high):
  if high>low:
    mid=(high-low)//2 + low
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge_subarray(arr,low,mid,high)

arr=[10,9,8,7,6,5,4,3,2,1]
merge_sort(arr,0,len(arr)-1)
print(arr)

#Constraints:
#Time complexity:O(nlogn)
#Auxilary Space:O(n)

