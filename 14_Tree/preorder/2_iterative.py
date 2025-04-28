# Implementation of preorder traversal by iterative approach
from collections import deque

def preorder(root):
  res = []
  s = []
  s.append(root)
  while s:
    temp = s[-1]
    res.append(s.pop().data)

    if temp.right:
      s.append(temp.right)
    if temp.left:
      s.append(temp.left)
  return res

#Node Class
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# function for tree construction
def construct(s):
  if len(s)==0 or s[0]=="N":
    return
  s = list(map(str, s.split()))
  q = deque()
  root = Node(int(s[0]))
  curr = root
  q.append(root)
  i = 1
  while q and (i < len(s)):
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

if __name__ == "__main__":
  s = input("Enter the input: ")
  root = construct(s)
  print(preorder(root))

#Constraints of preorder function
#Time Complexity: theta(n)
#Auxilary Space: theta(h)

