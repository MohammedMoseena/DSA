#Delete kt node of circular linked list
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

def deletefirstnode(head):
  if (head==None) or (head.next==head):
    return None
  head.data=head.next.data
  head.next=head.next.next
  return head

def deletektnode(head,k):
  if k==1:
    return deletefirstnode(head)
  curr=head
  for i in range(k-2):
    curr=curr.next
  curr.next=curr.next.next
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
head=deletektnode(head,2)
printcl(head)

#Time Complexity:O(K)
#Auxilary Space:O(1)