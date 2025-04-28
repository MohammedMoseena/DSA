#Reverse doubly linked list
class Node:
  def __init__(self,key):
    self.data=key
    self.next=None
    self.prev=None

def printDL(head):
  curr=head
  while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next

def reverse_DL(head):
  if (head==None):
    return None
  if (head.next)==None:
    return head
  curr=head
  while curr!=None:
    prev=curr
    curr.next,curr.prev=curr.prev,curr.next
    curr=curr.prev
  return prev

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
print("\n")
head=reverse_DL(head)
printDL(head)

#Constraints
#Time complexity:O(n)
#Auxilary Space:O(1)
