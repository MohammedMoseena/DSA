#Reverse the linked list using iterative method
class Node:
  def __init__(self,key):
    self.key=key
    self.next=None
def printlist(head):
  while head!=None:
    print(head.key,end=" ")
    head=head.next
def reverse_linked_list(head):
  prev=None
  curr=head
  while curr!=None:
    next=curr.next
    curr.next=prev
    prev=curr
    curr=next
  return prev
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head=reverse_linked_list(head)
printlist(head)

#Constraints
#Time Complexity:O(n)
#Aucilary Space:O(1)