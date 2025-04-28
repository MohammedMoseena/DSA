# Implementation of postorder using one stack be iterative approach
from collections import deque

def postorderutil(root, res):
  curr = root
  st = []
  while curr != None or st != []:
    if curr != None:
      st.append(curr)
      curr = curr.left
    else:
      temp = st[-1].right
      if temp == None:
        temp = st.pop()
        res.append(temp.data)
        while st != [] and temp == st[-1].right:
          temp = st.pop()
          res.append(temp.data)

      else:
        curr = temp

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


  #Constraints of postorderutil
  #Time Complexity: O(2*N)
  #Auxilary Space:O(h)