# Reverse a list in Python
def reverse_list(l):
  for i in range(0,len(l)//2):
    l[i],l[len(l)-i-1]=l[len(l)-i-1],l[i]
  return l

l=["geeks","ide","courses"]
print(reverse_list(l))

#Constraints:
#Time complexity: O(n)
#Space complexity:O(1)
#Auxilary Space:O(1)