def insertion_sort(arr,n):
  for i in range(1,n):
    temp=arr[i]
    j=i-1
    while j>=0 and arr[j]>temp:
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=temp
  return arr

arr=[10]
print(insertion_sort(arr,len(arr)))

#Best case: Sorted-O(n)
#Worst case: Reverse Sorted-O(n^2)
#Efficient for sorted or almost sorted arrays

#Constraints
#Time complexity:O(n^2)
#Auxilary Space:O(1)