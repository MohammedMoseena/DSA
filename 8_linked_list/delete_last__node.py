#Delete last Node of linked list

class Node:
  def __init__(self,key):
    self.key=key
    self.next=None

def printlinkedlist(head):
  curr=head
  while curr!=None:
    print(curr.key,end=" ")
    curr=curr.next

def deletelastnode(head):
  if (head==None) or (head.next==None):
    return None
  curr=head
  while head.next.next!=None:
    head=head.next
  head.next=None
  return curr


head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
# head.next.next.next=Node(40)
head= deletelastnode(head)
printlinkedlist(head)

#Constraints
#Time Complexity:O(n)
#Auxilar Space:O(1)