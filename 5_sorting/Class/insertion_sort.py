#Insertion Sort
'''
1. O(n^2)-worst case
2. in-place and stable
3. used in practice for small arrays(Timsort and Introsort)
4. O(n) in best case
5. works best for almost sorted or small lists
'''
def insertion_sort(arr,n):
  for i in range(1,n):
    temp=arr[i]
    j=i-1
    while j>=0 and temp<arr[j]:
      arr[j+1]=arr[j]
      j=j-1
    arr[j+1]=temp
  return arr
arr=[20,5,40,60,10,30]
print(insertion_sort(arr,len(arr)))

#Constraints
#Time complexity:O(n^2)
#Auxilary space:O(n)

'''
Note: 
Best Case: Sorted array->O(n)
Worst Case: Reverse sorted array->O(n^2)
'''