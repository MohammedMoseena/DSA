# Selection Sort
'''
1. Does less memory writes compared to 
Quick sort, merge sort, insertion sort etc but cycle sort is optimal in terms of memory writes
2. Basic idea for Heapsort
3. not stable(in basic form)
4. in-place(does not require extra space in sorting)
'''
# Selection sort works based on minimum element 
# selection sort is unstable

def selection_sort(arr,n):
  for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
      if arr[min_index]>arr[j]:
        min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
  return arr

arr=[90,80,90,25]
n=len(arr)
print(selection_sort(arr,n))

#Constraints:
#Time complexity:theta(n*n)
#auxilary space:O(1)