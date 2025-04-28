#Delete first node of circular linked list
class Node:
  def __init__(self,key):
    self.data=key 
    self.next=None
def printcl(head):
  if head==None:
    return None
  print(head.data,end=" ")
  curr=head.next
  while curr!=head:
    print(curr.data,end=" ")
    curr=curr.next

# def deletefirstnode(head):
#   if (head==None) or (head.next==head):
#     return None
#   curr=head
#   while curr.next!=head:
#     curr=curr.next
#   curr.next=head.next
#   head=head.next
#   return head

def deletefirstnode(head):
  if (head==None) or (head.next==head):
    return None
  head.data=head.next.data
  head.next=head.next.next
  return head
def insertEnd(head,x):
  new_node=Node(x)
  if head==None:
    new_node.next=new_node
    return new_node
  temp=head.next
  head.next=new_node
  new_node.next=temp
  new_node.data,head.data=head.data,new_node.data
  return new_node

head=None
head=insertEnd(head,10)
head=insertEnd(head,20)
head=insertEnd(head,30)
head=deletefirstnode(head)
printcl(head)

#Time Complexity:O(1)
#Auxilary Space:O(1)