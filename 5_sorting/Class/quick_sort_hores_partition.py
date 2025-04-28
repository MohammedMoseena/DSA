#Quick sort using hoares partition

def partition(arr,l,h):
  pivot=arr[l]
  i=l-1
  j=h+1
  while True:
    i=i+1
    while arr[i]<pivot:
      i+=1
    j=j-1
    while arr[j]>pivot:
      j-=1
    if i>=j:
      return j
    arr[i],arr[j]=arr[j],arr[i]

def quick_sort(arr,l,h):
  if l<h:
    p = partition(arr,l,h)
    quick_sort(arr,l,p)
    quick_sort(arr,p+1,h)

arr=[8,4,7,9,3,10,5]
l=0
h=len(arr)-1
quick_sort(arr,l,h)
print(arr)

#Constraints:
#Time complexity:
#Auxilary Space: