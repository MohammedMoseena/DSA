#Insert at given Position in Singly Linked List
class Node:
  def __init__(self,key):
    self.key=key
    self.next=None

def printlist(head):
  curr=head
  while curr!=None:
    print(curr.key,end=" ")
    curr=curr.next

def insert_position_linked_list(head,pos,data):
  temp=Node(data)
  if pos==1:
    temp.next=head
    return temp
  curr=head
  for i in range(pos-2):
    curr=curr.next
    if curr==None:
      return head
  temp.next=curr.next
  curr.next=temp
  return head

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
# printlist(head)
insert_position_linked_list(head,4,45)
printlist(head)

