#Implementation of inorder traversal of binary tree using recursive approach
from collections import deque

def inorderUtil(root,res):
  if root==None:
    return 
  inorderUtil(root.left,res)
  res.append(root.data)
  inorderUtil(root.right,res)

def inorder(root):
  res=[]
  inorderUtil(root,res)
  return res

#Class to construct node
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
#Function to construct tree
def construct(s):
  
  if len(s)==0 or s[0]=="N":
    return None
  s=list(map(str,s.split()))
  root=Node(int(s[0]))
  q=deque()
  q.append(root)
  i=1
  while (q!=[] and i<len(s)):
    currNode=q.popleft()
    #left Node
    if s[i]!="N":
      currNode.left=Node(int(s[i]))
      q.append(currNode.left)
    #Right Node
    i+=1
    if i<len(s):
      if s[i]!="N":
        currNode.right=Node(int(s[i]))
        q.append(currNode.right)
    else:
      break 
    i+=1
  return root

#driver code
if __name__ == "__main__":
  s = input("Please enter input:")
  root = construct(s)
  res = inorder(root)
  print(res)


# Constraints of inorderUtil fun
#Time Complexity: O(n)
#Auxilary Space: O(h) h: height of tree which is maximum distance from root to leaf node