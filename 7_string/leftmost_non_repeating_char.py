# Left Most Non Repeating Charater
import sys
def left_most_non_repeating_char(s):
  track_list=[-1]*256
  for i in range(len(s)):
    if track_list[ord(s[i])]==-1:
      track_list[ord(s[i])]=i
    else:
      track_list[ord(s[i])]=-2
  res=sys.maxsize
  for i in range(len(track_list)):
    if track_list[i]>=0:
      res=min(res,track_list[i])
  if res==sys.maxsize:
    return -1
  else:
    return res

s="apple"
print(left_most_non_repeating_char(s))

#Constraints:
#Time Complexity:O(n)
#Auxilary Space:O(1)