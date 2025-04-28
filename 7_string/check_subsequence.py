#Subsequence and substring are different
#Subsequence- order should be maintained
#Substring-order should be maintained and alos continous characters
#For evry string we will have 2^n subsequences

def check_subsequence(s1,s2):
  i=0
  j=0
  while (i<len(s1)) and (j<len(s2)):
    if s2[j]==s1[i]:
      j+=1
    i+=1
  if j==len(s2):
    return True
  else:
    return False
  
'''
#Recursive Method
def recursive_sub_sequence(s1,s2,m,n):
  if n==0:
    return True
  elif m==0:
    return False
  elif s1[m]==s2[n]:
    return recursive_sub_sequence(s1,s2,m-1,n-1)
  else:
    return recursive_sub_sequence(s1,s2,m-1,n)

'''

s1="ABCDE"
s2="ACD"
print(check_subsequence(s1,s2))
# print(recursive_sub_sequence(s1,s2,len(s1)-1,len(s2)-1))

#Constraints
#Time Complexity:O(n)
#Auxilary Space:O(1)



  