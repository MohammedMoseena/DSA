#Leftmost Repeating Character
def leftmost_repeating_character(s):
  count_list=[0]*256
  for item in s:
    count_list[ord(item)]+=1
  for i in range(len(s)):
    if count_list[ord(s[i])]>1:
      return i
  else:
    return -1

def efficient_leftmost_repeating_characted(s):
  track_list=[False]*256
  res=-1
  for i in range(len(s)-1,-1,-1):
    if track_list[ord(s[i])]==True:
      res=i
    else:
      track_list[ord(s[i])]=True
  return res
  
s="abccbd"
# print(leftmost_repeating_character(s))
print(efficient_leftmost_repeating_characted(s))


#Constraints:
#Time Complexity:O(n)
#Auxilary Space:O(c)