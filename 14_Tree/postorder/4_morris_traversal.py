# Implementation of postorder by morris traversal
from collections import deque

#postorder morris traversal

def postorderutil(root, res):
  curr = root
  while curr != None:
    if curr.right == None:
      res.append(curr.data)
      curr = curr.left
    else:
      prev = curr.right
      while (prev.left != None) and (prev.left != curr):
        prev = prev.left
      if prev.left == None:
        prev.left = curr
        res.append(curr.data)
        curr = curr.right
      if prev.left == curr:
        prev.left = None
        curr = curr.left

def postorder(root):
  res = []
  postorderutil(root, res)
  # Reversal the result
  # for i in range(0, len(res)//2):
  #   res[i], res[len(res)-1-i] = res[len(res)-1-i], res[i]
  return res[::-1]

#Node Class
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

#Function for tree construction
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
    #Left Node
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
  s = input("Enter the input:")
  root = construct(s)
  print(postorder(root))


#Constraints of postorderutil:
#Time Complexity: O(N)
#Auxilary Space: O(1)