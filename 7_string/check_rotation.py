#Given two strings check whether one string is obtained by rotating second string single or multiple times

def check_rotation(s1,s2):
  if len(s1)!=len(s2):
    return False
  for i in range(len(s1)):
    if (s1[i+1:]+s1[i:i+1])==s2:
      return True
  else:
    return False
  
s1="ABAB"
s2="ABBA"
print(check_rotation(s1,s2))

#Constraints:
#Time complexity:O(n)
#Auxilary Space:O(1)