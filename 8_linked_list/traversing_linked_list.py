#Traversing a Linked List in Python
class Node:
  def __init__(self,k):
    self.key=k
    self.next=None
def traversing(head):
  curr=head
  while curr!=None:
    print(curr.key,end=" ")
    curr=curr.next
# Driver Code
# head=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(15)
head.next.next.next=Node(30)

#Traversing the code
traversing(head)

#Constraints:
#Time complexity:theta(n)
#Aucilary Space:theta(1)

