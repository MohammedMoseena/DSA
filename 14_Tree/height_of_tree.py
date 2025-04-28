# Find of the height of the tree
from collections import deque

def height(root):
  if not root:
    return -1
  return 1 + max(height(root.left), height(root.right))
# Node Class
class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

#Function for construction of tree
def construction(s):
  if len(s) == 0 or s[0] == "N":
    return None
  s = list(map(str, s.split()))
  root = Node(int(s[0]))
  q = deque()
  q.append(root)
  i = 1
  while q and i < len(s):
    currroot = q.popleft()
    # Left Node
    if s[i] != "N":
      currroot.left = Node(int(s[i]))
      q.append(currroot.left)
    i+=1
    # Right Node
    if i < len(s):
      if s[i] != "N":
        currroot.right = Node(int(s[i]))
        q.append(currroot.right)
    else:
      break
    i+=1
  return  root
  
if __name__ == "__main__":
  s = input("Enter the input: ")
  root = construction(s)
  print(height(root))

# Constraints of height:
# time complexity: theta(n)
# Auxilary Space: theta(h) where h is height of binary tree
