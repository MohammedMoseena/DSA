#Count of inversions
def count_merge(arr,low,mid,high):
  left=arr[low:mid+1]
  right=arr[mid+1:high+1]
  i=0
  j=0
  k=low
  count=0
  while i<len(left) and j<len(right):
    if left[i]<=right[j]:
      arr[k]=left[i]
      i+=1
      k+=1
    else:
      arr[k]=right[j]
      count+=len(left)-i
      k+=1
      j+=1
  while i<len(left):
    arr[k]=left[i]
    i+=1
    k+=1
  while j<len(right):
    arr[k]=right[j]
    j+=1
    k+=1
  return count

def count_of_inversions(arr,low,high):
  count=0
  if high>low:
    mid=(high-low)//2+low
    count+=count_of_inversions(arr,low,mid)
    count+=count_of_inversions(arr,mid+1,high)
    count+=count_merge(arr,low,mid,high)
  return count


arr=[40,30,20,10]
low=0
high=len(arr)-1
print(count_of_inversions(arr,low,high))

#Constraints:
#Time complexity:theta(nlogn)
#Auxilary Space:O(n)