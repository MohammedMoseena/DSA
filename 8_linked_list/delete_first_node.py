#Delete first node of linked list
class Node:
  def __init__(self,key):
    self.key=key
    self.next=None
def printlinkedlist(head):
  curr=head
  while curr!=None:
    print(curr.key,end=" ")
    curr=curr.next
def delete_first_node(head):
  if head==None:
    return None
  return head.next


head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
# head.next.next.next=Node(40)

head=delete_first_node(head)
printlinkedlist(head)

#Constraints
#Time Complexity:O(1)
#Axilary Space:O(1)
