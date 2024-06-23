# Check if list is sorted or not
#This method is much efficient than using sorted function
def check_for_sort(l):
  if len(l)<=1:
    return False
  
  for i in range(1,len(l)):
    if l[i]<l[i-1]:
      return False
  else:
    return True 

l=[10,5,30]
print(check_for_sort(l))

#Constraints:
#Time complexity:O(n)
#Space Complexity:O(1)