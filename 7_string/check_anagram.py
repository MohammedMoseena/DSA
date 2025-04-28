'''
Anagram: An anagram of a string is another string that contains the same characters, only the order of characters can be different
'''

def check_for_anagram(s1,s2):
  if len(s1)!=len(s2):
    return False
  count=[0]*256
  for i in range(len(s1)):
    count[ord(s1[i])]+=1
    count[ord(s2[i])]-=1
  for x in count:
    if x!=0:
      return False
  return True

s1="aab"
s2="abb"
print(check_for_anagram(s1,s2))

#Constranits:
#Time Complexity:O(n) 
#Auxilary space:O(c)