#Implementation of inorder traversal by morris traversal
from collections import deque

def inorderUtil(root, res):
  if root == None:
    return
  curr = root
  while curr != None:
    if curr.left == None:
      res.append(curr.data)
      curr = curr.right
    
    else:
      prev = curr.left
      while (prev.right != None) and (prev.right != curr):
        prev = prev.right
      
      if prev.right == None:
        prev.right = curr
        curr = curr.left
      
      if prev.right == curr:
        prev.right = None
        res.append(curr.data)
        curr = curr.right


def inorder(root):
  res = []
  inorderUtil(root, res)
  return res


# Node Class
class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

#Function for constructing tree
def construct(s):
  if len(s) == 0 or s[0] == "N":
    return
  s = list(map(str, s.split()))
  root = Node(int(s[0]))
  q = deque()
  q.append(root)
  i = 1
  while q != [] and i < len(s):
    currNode = q.popleft()
    #Left Node
    if s[i] != "N":
      currNode.left = Node(int(s[i]))
      q.append(currNode.left)
    
    #Right Node
    i+=1
    if i < len(s):
      if s[i] != "N":
        currNode.right = Node(int(s[i]))
        q.append(currNode.right)
    else:
      break
    i+=1
  return root

if __name__ ==  "__main__":
  s = input("Enter the input:")
  root = construct(s)
  res = inorder(root)
  print(res)


#Constraints of inorderUtil
#Time Complexity : O(n)
#Auxilary Space: O(1)



  
