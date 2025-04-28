# Implementation of pre order by recursive approach
from collections import deque

#Preorder traversal
def preorderutil(root, res):
  if not root:
    return
  res.append(root.data)
  preorderutil(root.left, res)
  preorderutil(root.right, res)

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

# Function to construct tree
def construct(s):
  if len(s) == 0 or s[0] == "N":
    return None
  s = list(map(str, s.split()))
  root = Node(int(s[0]))
  q = deque()
  q.append(root)
  i=1
  while q and i < len(s):
    curr = q.popleft()
    # Left Node
    if s[i] != "N":
      curr.left = Node(int(s[i]))
      q.append(curr.left)
    #Right Node
    i+=1
    if i < len(s):
      if s[i] != "N":
        curr.right = Node(int(s[i]))
        q.append(curr.right)
    else:
      break
    i+=1
  return root

if __name__ == "__main__":
  s = input("enter your input:")
  root = construct(s)
  print(preorder(root))

