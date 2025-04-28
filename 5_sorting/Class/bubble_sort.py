# Bubble sort bubbling up the maximum element
# For every ith pass/ith traversal we get ith maximum

# Bubble sort is stable algorithm
#Bubble sort works on swapping adjacent elements

def bubble_sort(arr,n):
  swapped=False
  for i in range(n-1):
    for j  in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
        swapped=True
    if swapped==False:
      return arr
  return arr

    

arr=[10,8,20,5]
n=len(arr)
print(bubble_sort(arr,n))

#Constraints:
#Time complexity:O(n*n)
#auxilary space:O(1)

