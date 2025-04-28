#Middle of a linked list
class Node:
  def __init__(self,key):
    self.key=key
    self.next=None
def printlist(head):
  while head!=None:
    print(head.key,end=" ")
    head=head.next
def middle_of_linked_list(head):
  if (head==None) or (head.next==None):
    return head
  slow=head
  fast=head
  while (fast!=None) and (fast.next!=None):
    slow=slow.next
    fast=fast.next.next
  return slow.key

head=Node(10)
head.next=Node(5)
head.next.next=Node(20)
head.next.next.next=Node(15)
head.next.next.next.next=Node(25)
print(middle_of_linked_list(head))

#Constraints
#Time Complexity: O(n)
#Auxilary Space:O(1)