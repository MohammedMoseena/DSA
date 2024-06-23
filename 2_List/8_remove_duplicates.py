# Remove Duplicates from a Sorted Array
arr=[10,10,10]

def remove_duplicates(arr):
  res=1
  for i in range(1,len(arr)):
    if arr[i]!=arr[res-1]:
      arr[res]=arr[i]
      res+=1
  return res

end=remove_duplicates(arr)
print(arr[0:end])
  
#Time complexity:O(n)
#Auxilary Space:O(1)