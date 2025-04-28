#lomuto Partition
#last element of array is pivot
def lomuto_partition(arr,l,h):
  pivot=arr[h]
  i=l-1
  for j in range(len(arr)):
    if arr[j]>=pivot:
      continue
    else:
      arr[i+1],arr[j]=arr[j],arr[i+1]
      i+=1
  arr[i+1],arr[h]=arr[h],arr[i+1]

  return i+1

arr=[10,80,30,90,40,50,70]
l=0
h=len(arr)-1
print(lomuto_partition(arr,l,h))

#Constraints
#Time complexity:O(n)-1 traversal
#Auxilary Space:O(1)