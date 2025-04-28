#Union of two sorted arrays
def union_of_sorted_arr(arr1,arr2):
  i=0
  j=0
  res=[]
  while i<len(arr1) and j<len(arr2):
    if (i>0 and arr1[i]==arr1[i-1]):
      i+=1
    elif (j>0 and arr2[j]==arr2[j-1]):
      j+=1
    elif arr1[i]<arr2[j]:
      res.append(arr1[i])
      i+=1
    elif arr1[i]>arr2[j]:
      res.append(arr2[j])
      j+=1
    else:
      res.append(arr1[i])
      i+=1
      j+=1

  while i<len(arr1):
    if arr1[i]!=arr1[i-1]:
      res.append(arr1[i])
    i+=1
  while j<len(arr2):
    if arr2[j]!=arr2[j-1]:
      res.append(arr2[j])
    j+=1
  print('hi')
  return res

arr1=[2,3,3,3]
arr2=[3,4,4]
print(union_of_sorted_arr(arr1,arr2))


