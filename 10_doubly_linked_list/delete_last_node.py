# Delete Last Node of Doubly Linked List
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
def insertAtBegin(head,x):
  temp=Node(x)
  if head!=None:
    head.prev=temp
  temp.next=head
  return temp
def deletelastnode(head):
  if (head==None) or (head.next==None):
    return None
  curr=head
  while curr.next.next!=None:
    curr=curr.next
  curr.next=None
  return head




head=None
head=insertAtBegin(head,10)
# head=insertAtBegin(head,20)
# head=insertAtBegin(head,30)
printDL(head)
print("\n")

deletelastnode(head)
printDL(head)

#Constraints
#Time Complexity:O(n)
#Auxilary Space:O(1)