# Sorted insert in a linked list
class Node:
  def __init__(self,key):
    self.key=key
    self.next=None
def printlist(head):
  while head!=None:
    print(head.key,end=" ")
    head=head.next
def sorted_insert(head,data):
  new_node=Node(data)
  if head==None:
    return new_node
  elif head.key>new_node.key:  #Minimum condition
    new_node.next=head
    return new_node
  curr=head
  while curr.next!=None:
    if curr.next.key>new_node.key:      
      new_node.next=curr.next
      curr.next=new_node
      return head
    curr=curr.next
  curr.next=new_node
  return head

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
printlist(head)
head=sorted_insert(head,55)
print('\n')
printlist(head)

#Constraints:
#Time Complexity:O(n)
#Auxilary Space:O(1)
