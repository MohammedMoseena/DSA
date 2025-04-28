#Insert at the end of linked list
class Node:
  def __init__(self,key):
    self.key=key
    self.next=None

def printlinkedlist(head):
  curr=head
  while curr!=None:
    print(curr.key,end=" ")
    curr=curr.next

def insert_at_end(head,key):
  obj=Node(key)
  if head==None:
    head=obj
  else:
    curr=head
    while head.next!=None:
      head=head.next
    head.next=obj
    head=curr
  return head

head=None
head=insert_at_end(head,10)
head=insert_at_end(head,20)
head=insert_at_end(head,30)
printlinkedlist(head)