# Merge Two sorted lists
def merge_two_sorted_lists(a,b,m,n):
  res=[]
  i=0
  j=0
  while i<m and j<n:
    if a[i]>b[j]:
      res.append(b[j])
      j+=1
    else:
      res.append(a[i])
      i+=1
  while i<m:
    res.append(a[i])
    i+=1
  while j<n:
    res.append(b[j])
    j+=1
  return res


a=[10,15,20]
b=[5,6,6,30]
print(merge_two_sorted_lists(a,b,len(a),len(b)))

#Constraints:
#Time complesity:O(a+b)
#Auxilary space:O(a+b)