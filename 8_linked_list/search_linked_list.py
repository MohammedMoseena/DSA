#Search in Linked List
class Node:
  def __init__(self,k):
    self.key=k
    self.next=None
def search(head,x):
  curr=head
  i=0
  while curr!=None:
    if curr.key==x:
      return i
    curr=curr.next
    i+=1
  return -1
#Driver Code
head=Node(10)
head.next=Node(5)
head.next.next=Node(30)
# head.next=Node(15)

print(search(head,10))

#Constraints:
#Time Complexity:O(n)
#Auxilary Space:O(1)