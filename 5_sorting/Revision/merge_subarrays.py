#Merge two sorted subarrays to get final sorted array
def merge_subarray(arr1,arr2):
  i=0
  j=0
  res=[]
  while i<len(arr1) and j<len(arr2):
    if arr1[i]<=arr2[j]:
      res.append(arr1[i])
      i+=1
    else:
      res.append(arr2[j])
      j+=1
  while i<len(arr1):
    res.append(arr1[i])
    i+=1
  while j<len(arr2):
    res.append(arr2[j])
    j+=1
  return res

arr1=[5,6,11,11,12,13]
arr2=[5,10,20,30,40,60]
print(merge_subarray(arr1,arr2)) 

#Constraints:
#Time complexity:theta(m+n)
#Auxilary Space:theta(m+n)