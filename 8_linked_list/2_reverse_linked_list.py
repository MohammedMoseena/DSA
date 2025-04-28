#Reverse linked list using recursive method
#Method1- Reversing the list from right to left
class Node:
  def __init__(self,key):
    self.key=key
    self.next=None
def printlinkedlist(head):
  while head!=None:
    print(head.key,end=" ")
    head=head.next
def reverse_linked_list(head):
  if head==None:
    return None
  if head.next==None:
    return head
  rest_head=reverse_linked_list(head.next)
  rest_tail=head.next
  rest_tail.next=head
  head.next=None
  return rest_head

head=None
# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
# head.next.next.next=Node(40)
print("Original Linked List:",end=" ")
printlinkedlist(head)
print("\n")
print("Reversing Linked List:",end=" ")
head=reverse_linked_list(head)
printlinkedlist(head)


#Constraints:
#Time Complexity:O(n)
#Auxilary Space:O(n)