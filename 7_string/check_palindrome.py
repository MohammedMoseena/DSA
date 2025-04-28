#Check if given string is palindrome or not
def check_palindrome(s):
  if len(s)==1:
    return True
  low=0
  high=len(s)-1
  while low<=high:
    if s[low]!=s[high]:
      print('No')
    low=low+1
    high=high-1
  else:
    print('Yes')
s="aBA"
print(check_palindrome(s))

#Constraints
#Time Complexity:O(n)
#Auxilary Space:O(1)