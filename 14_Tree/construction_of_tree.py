#Construction of tree from list
from collections import deque
#class to construct node
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
#Function to construct tree from the input
def construct(s):
  if len(s)==0 or s[0]=="N":
    return None
  root = Node(s[0]) #Root Node
  q=deque()
  q.append(root)
  i=1
  while (q!=[] and i<len(s)):
    currNode=q.popleft()
    #left Node
    currVal=s[i]
    if currVal!="N":
      currNode.left=Node(currVal)
      q.append(currNode.left)
    #Right Node
    i+=1
    if i<len(s):
      currVal=s[i]
      if currVal!="N":
        currNode.right=Node(currVal)  
        q.append(currNode.right) 
      i+=1 
    else:
      break
  return root

#driver code
if __name__ == "__main__":
  t = int(input())
  for _ in range(0,t):
    s=list(input())
    root=construct(s)
    # You can write here traversal code refrencing to the root

#constraints:
#Time Complexity:O(n)
#Auxilary Space: O(w) w-width of the tree

