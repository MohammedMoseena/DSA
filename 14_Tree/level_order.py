# Level Order traversal
from collections import deque
def levelorderutil(root, ans):
  if not root:
    return
  q = deque()
  q.append(root)
  ans.append([root.data])
  while q:
    l1 = []
    currRoot = q.popleft()
    if currRoot.left:
      l1.append(currRoot.left.data)
      q.append(currRoot.left)
    if currRoot.right:
      l1.append(currRoot.right.data)
      q.append(currRoot.right)
    if l1!=[]:
      ans.append(l1)
  return ans

def levelorder(root):
  ans = []
  levelorderutil(root, ans)
  return ans

#Node Class
class Node:
  def __init__(self,data):
    self.data = data 
    self.left = None
    self.right = None

#Function to construct tree from list
def construct(s):
  if len(s) == 0 or s[0]=="N":
    return None
  s = list(map(str, s.split()))
  root = Node(int(s[0]))
  q = deque()
  q.append(root)
  i = 1
  while q and (i < len(s)):
    #Current Root Node
    currroot = q.popleft()
    #Current Left Node
    if s[i] != "N":
      currroot.left = Node(int(s[i]))
      q.append(currroot.left)
    #Currnet Right Node
    i+=1
    if i < len(s):
      if s[i] != "N":
        currroot.right = Node(int(s[i]))
        q.append(currroot.right)
    else:
      break
    i+=1
  return root

if __name__ == "__main__":
  s = input("Enter your input:")
  root = construct(s)
  print("Output: ", levelorder(root))

#Constraints of levelorderutil
#Time Complexity:theta(n)
#Auxilary Space:O(w) where w is the width/level of the tree

