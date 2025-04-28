# Insert elements into binary search tree

#Node Class
class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

'''
#Recursive Insert Function
def insert(root, x):
  if root == None:
    return Node(x)
  if root.data == x:
    return root
  if root.data > x:
    root.left = insert(root.left, x)
  if root.data < x:
    root.right = insert(root.right, x)
  return root
#Constraints:
#Time Complexity: O(h)
#Auxilary Space: O(h)
'''
#Iterative Approach
def insert(root, x):
  if root == None:
    return Node(x)
  if root.data == x:
    return root
  curr = root
  while curr:
    if curr.data == x:
      break
    if curr.data > x:
      prev = curr
      curr = curr.left
    else:
      prev = curr
      curr = curr.right
  if curr == None:
    if prev.data > x:
      prev.left = Node(x)
    else:
      prev.right = Node(x)
  return root


#Preorder traversal
def preorder(root):
  if root == None:
    return 
  print(root.data,end=" ")
  preorder(root.left)
  preorder(root.right)

root = insert(None, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 20)
preorder(root)
  
#Constraints:
#Time Complexity:O(h)
#Auxilary Space:O(1)