#Partition a given Array

def partition_array(arr,p):
  n=len(arr)
  arr[p],arr[n-1]=arr[n-1],arr[p]
  temp=[]
  for item in arr:
    if item<=arr[n-1]:
      temp.append(item)
  for item in arr:
    if item>arr[n-1]:
      temp.append(item)
  for i in range(len(arr)):
    arr[i]=temp[i]

arr=[5,13,6,9,12,8,11]
partition_array(arr,5)
print(arr)

#Constraints:
#Time complexity:O(n)-3traversals
#Auxilary Space:O(n)







l=[3,8,6,12,10,7]
