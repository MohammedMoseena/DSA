def selection_sort(arr,n):
  for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
      if arr[min_index]>arr[j]:
        min_index=j
    if min_index!=i:
      arr[min_index],arr[i]=arr[i],arr[min_index]
  return arr

arr=[1]
print(selection_sort(arr,len(arr)))

#Worst Case & Best Case:theta(n^2)
#Constraints
#Time complexity:theta(n^2)
#Auxilary space:theta(1)