#Implementation of inorder traversal by iterative approach
from collections import deque

#Iterative approach for inorder traversal
def inorderUtil(root, res):
  if root == None:
    return
  s = []
  curr = root
  while True:
    if curr != None:
      s.append(curr)
      curr = curr.left
    else:
      if s == []:
        break
      else:
        temp = s.pop()
        res.append(temp.data)
        curr=temp.right
  
def inorder(root):
  res = []
  inorderUtil(root, res)
  return res

#Construct node class
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

#Function for tree construction from list/string
def construct(s):
  s = list(map(str,s.split()))
  if len(s) == 0 or s[0] == "N":
    return 
  root = Node(int(s[0]))
  q = deque()
  q.append(root)
  i=1
  while q != [] and i < len(s):
    currNode = q.popleft()
    #left Node
    if s[i] != "N":
      currNode.left = Node(int(s[i]))
      q.append(currNode.left)
    #right Node
    i+=1
    if i<len(s):
      if s[i] != "N":
        currNode.right = Node(int(s[i]))
        q.append(currNode.right)
    else:
      break
    i+=1
  
  return root

#Driver Code
if __name__ ==  "__main__":
  s = input("Enter the input: ")
  root = construct(s)
  print(inorder(root))

#Constraints of inorderUtil
#Time Complexity : O(n)
#Auxilary Space: O(h)



