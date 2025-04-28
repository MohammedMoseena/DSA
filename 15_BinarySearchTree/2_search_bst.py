# Search an element in binary search tree
#Node Class
class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
'''
#Recursive Method
def search_bst(root, x):
  if (root == None) or (root.data == x):
    return root
  if x < root.data:
    search_bst(root.left, x)
  else:
    search_bst(root.right, x)

#Constraints:
#Time complexity: O(h)
#Auxilary Space:O(h)
'''

#Iterative Method
def search_bst(root, x):
  curr = root
  while curr:
    if x == curr.data:
      return True
    elif x > curr.data:
      curr = curr.right
    else:
      curr = curr.left
  return 

#Constraints:
#Time complexity: O(h)
#Auxilary Space:O(1)

def insert(root, x):
  if (root == None):
    return Node(x)
  if root.data == x:
    return root
  curr = root
  prev = None
  while curr:
    if curr.data == x:
      break
    if curr.data < x:
      prev = curr
      curr = curr.right
    else:
      prev = curr
      curr = curr.left
  if curr == None:
    if prev.data > x:
      prev.left = Node(x)
    elif prev.data < x:
      prev.right = Node(x)
  return root

def preorder(root):
  if root == None:
    return
  print(root.data, end = " ")
  preorder(root.left)
  preorder(root.right)


root = insert(None, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 12)
root = insert(root, 18)
preorder(root)
print(search_bst(root, 12))

