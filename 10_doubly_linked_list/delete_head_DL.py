# Delet head of a doubly linked list
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
def deleteHead(head):
  if (head==None) or (head.next==None):
    return None
  head.next.prev=None
  return head.next

def insertAtBegin(head,x):
  temp=Node(x)
  if head!=None:
    head.prev=temp
  temp.next=head
  return temp
head=None
head=insertAtBegin(head,10)
head=insertAtBegin(head,20)
# head=insertAtBegin(head,30)
printDL(head)
print("\n")

head=deleteHead(head)
printDL(head)

#Time Complexity:O(1)
#Auxilary Space:O(1)