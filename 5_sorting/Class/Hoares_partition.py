#Hoares Partition
def hoeres_partition(arr,l,h):
  pivot=arr[l]
  i=l-1
  j=h+1
  while True:
    i=i+1
    while arr[i]<pivot:
      i+=1
    j=j-1
    while arr[j]>pivot:
      j-=1
    if i>=j:
      return j
    arr[i],arr[j]=arr[j],arr[i]
  
#arr=[5,3,8,4,2,7,1,10]
#Corner cases
#Corner case-1:Pivot is smallest in arr
#arr=[5,10,9,12]
#Corner case-2:Pivot is larvets in arr
#arr=[12,10,5,9]
#Corner Case-3: All Elements are same
arr=[5,5,5,5]

l=0
h=len(arr)-1
print(hoeres_partition(arr,l,h))
print(f"Modified array:{arr}")

#Constraints:
#Time complexity:O(n)
#Auxilary Space: O(1)

