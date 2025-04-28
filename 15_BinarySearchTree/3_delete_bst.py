# Deletion in binary serach tree
class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

def insert(root, x):
  if root == None:
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
    if prev.data < x:
      prev.right = Node(x)
    elif prev.data > x:
      prev.left = Node(x)
  return root

def preorder(root):
  if root == None:
    return
  print(root.data, end = " ")
  preorder(root.left)
  preorder(root.right)

def getSucc(root):
  while root.left:
    root = root.left
  return root.data
  

#Deletion of node in BST
def delete(root, x):
  if root == None:
    return
  elif root.data > x:
    root.left = delete(root.left, x)
  elif root.data < x:
    root.right = delete(root.right, x)
  else:
    if root.left == None:
      return root.right
    if root.right == None:
      return root.left
    else:
      succ = getSucc(root.right)
      root.data = succ
      root.right = delete(root.right, succ)
  return root

root = insert(None, 1)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 5)
root = insert(root, 11)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 9)
root = insert(root, 12)
print("Before deletion: ")
preorder(root)
root = delete(root, 11)

print("\nAfter deletion: ")
preorder(root)