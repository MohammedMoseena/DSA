# Delet a node with only pointer given to it
class Node:
  def __init__(self,key):
    self.key=key
    self.next=None
def printlist(head):
  curr=head
  while curr!=None:
    print(curr.key,end=" ")
    curr=curr.next
def delete_node_position(address):
  temp=address.next
  address.key=temp.key
  address.next=temp.next

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(25)
printlist(head)

#Constraints
#Time Complexit:O(1)
#Auxilary Space:O(1)