def bubble_sort(arr,n):
  swap=False
  for i in range(n-1):
    for j in range(0,n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
        swap=True
    if swap==False:
      return arr
  return arr

arr=[1]
print(bubble_sort(arr,len(arr)))

#Worst Case-Reverse sorted array-O(n^2)
#Best Case-Sorted array-O(n)

#Time constraints
#Time complexity:O(n^2)
#Auxilary Space:O(1)