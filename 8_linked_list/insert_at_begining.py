#Insert at the beginning of linked list
class Node:
  def __init__(self,key):
    self.key=key
    self.next=None

def printlinkedlist(head):
  curr=head
  while curr!=None:
    print(curr.key,end=" ")
    curr=curr.next


def insert_begin(head,key):
  obj=Node(key)
  obj.next=head
  head=obj
  return head

#Driver Code
head=None
# head.next=Node(20)
# head.next.next=Node(30)
head= insert_begin(head,10)
head= insert_begin(head,20)
head= insert_begin(head,30)
printlinkedlist(head)
#Constraints:
#Time Complexity:theta(1)
#Auxilary Space:theta(1)