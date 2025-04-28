#Implementation of preorder by recursive method
from collections import deque

def postorderutil(root, res):
  if root == None:
    return
  postorderutil(root.left, res)
  postorderutil(root.right, res)
  res.append(root.data)

def postorder(root):
  res = []
  postorderutil(root, res)
  return res


#Node Class
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# Tree construction function
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

    #left node
    if s[i] != "N":
      curr.left = Node(int(s[i]))
      q.append(curr.left)
    
    #Right node
    i+=1
    if i< len(s):
      if s[i] != "N":
        curr.right = Node(int(s[i]))
        q.append(curr.right)
    else:
      break
    i+=1
  return root

if __name__ == "__main__":
  s = input("Enter the input:")
  root = construct(s)
  print(postorder(root))
  

