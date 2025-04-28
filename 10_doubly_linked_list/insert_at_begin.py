#Insert at the beginning of Doubly linked list
class Node:
  def __init__(self,key):
    self.data=key
    self.prev=None
    self.next=None

def printDL(head):
  curr=head
  while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next

def insertAtBegin(head,x):
  temp=Node(x)
  if head!=None:
    head.prev=temp
  temp.next=head
  return temp
head=None
head=insertAtBegin(head,10)
head=insertAtBegin(head,20)
head=insertAtBegin(head,30)
printDL(head)

#Constraints
#Time Complexity:O(1)
#Auxilary Space:O(1)