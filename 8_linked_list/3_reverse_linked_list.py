#Reverse linked list using recursive method
#Method2- Reversing the list from left to right

class Node:
  def __init__(self,key):
    self.key=key
    self.next=None
def printlinkedlist(head):
  while head!=None:
    print(head.key,end=" ")
    head=head.next
def reverse_linked_list(curr,prev=None):
  if curr==None:
    return prev
  next=curr.next
  curr.next=prev
  return reverse_linked_list(next,curr)
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
print("Original Linked List:",end=" ")
printlinkedlist(head)
print("\n")
print("Reversing Linked List:",end=" ")
head=reverse_linked_list(head)
printlinkedlist(head)

#Constraints:
#Time Complexity:theta(n)
#Auxilary Space:O(n)