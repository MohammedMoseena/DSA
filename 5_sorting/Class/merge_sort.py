'''
Merge Sort
1. Divide and Conquer algorithm
(Divide,Conquer and merge)

2. Stable Algorithm

3. theta(nlogn) Time complexity and O(n) Auxilary space

4. Well suited for linked lists. works in O(1) Aux space

5. Used in External sorting

6. In general for arrays quick sort out performs merge sort

7. In python most of libraries use tim sort
'''
def merge_subarray(arr,low,mid,high):
  left=arr[low:mid+1]
  right=arr[mid+1:high+1]
  i=0
  j=0
  k=low
  while i<len(left) and j<len(right):
    if left[i]<=right[j]:
      arr[k]=left[i]
      k+=1
      i+=1
    else:
      arr[k]=right[j]
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

def merge_sort(arr,low,high):
  if high>low:
    mid=(high-low)//2 + low
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge_subarray(arr,low,mid,high)

arr=[10,5,30,15,7]
low=0
high=len(arr)-1
mid=(high-low)//2 + low
merge_sort(arr,low,high)
print(arr)


#Constraints:
#Time complexity:O(nlogn)
#Auxilary space:O(n)
