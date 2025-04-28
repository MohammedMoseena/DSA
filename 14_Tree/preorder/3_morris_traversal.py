#Implementation of preorder traversal by morris method
from collections import deque

def preorderutil(root, res):
  curr = root
  while curr:
    if curr.left == None:
      res.append(curr.data)
      curr = curr.right
    else:
      prev = curr.left
      while (prev.right != None) and (prev.right != curr):
        prev = prev.right
      
      if prev.right == None:
        prev.right = curr
        res.append(curr.data)
        curr = curr.left
      
      if prev.right == curr:
        prev.right = None
        curr = curr.right


def preorder(root):
  res = []
  preorderutil(root, res)
  return res
  
#Node Class
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

#Construction of Tree
def construct(s):
  if len(s) == 0 or s[0] == "N":
    return 
  s = list(map(str, s.split()))
  root = Node(int(s[0]))
  q = deque()
  q.append(root)
  i = 1
  while q and i < len(s):
    curr = q.popleft()
    # left Node
    if s[i] != "N":
      curr.left = Node(int(s[i]))
      q.append(curr.left)
    #right node
    i += 1
    if i < len(s):
      if s[i] != "N":
        curr.right = Node(int(s[i]))
        q.append(curr.right)
    else:
      break
    i+=1
  return root

if __name__ == "__main__":
  s = input("Enter the input: ")
  root = construct(s)
  print(preorder(root))

#Constraints of preorderutil function
#Time Complexity : theta(n)
#Auxilary Space: O(1)


    

