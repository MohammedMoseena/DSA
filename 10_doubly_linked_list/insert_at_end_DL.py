# Insert at the end of Linked List
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
  
def insertAtEnd(head,x):
  temp=Node(x)
  if head==None:
    return temp
  curr=head
  while curr.next!=None:
    curr=curr.next
  curr.next=temp
  temp.prev=curr
  temp.next=None
  return head


head=None
head=insertAtEnd(head,10)
head=insertAtEnd(head,20)
head=insertAtEnd(head,30)
printDL(head)

#Constraints:
#Time Complexity:O(n)
#Auxilary Space:O(1)