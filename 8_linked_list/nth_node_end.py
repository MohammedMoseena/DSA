#Find nth Node from end of linked list
class Node:
  def __init__(self,key):
    self.key=key
    self.next=None
def printlist(head):
  while head!=None:
    print(head.key,end=" ")
    head=head.next
#Method-1
# def nth_node_end(head,n):
#   count=0
#   curr=head
#   while curr!=None:
#     curr=curr.next
#     count+=1
#   if count<n:
#     return None
#   elif count==n:
#     return head.key
#   curr=head
#   for i in range(1,count-n+1):
#     curr=curr.next
#   return curr.key
# Method-2
def nth_node_end(head,n):
  if head==None:
    return None
  first=head
  for i in range(1,n+1):
    if first==None:
      return None
    first=first.next
  second=head
  while first!=None:
    first=first.next
    second=second.next
  return second.key
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
# head.next.next.next=Node(40)
# head.next.next.next.next=Node(50)
# head.next.next.next.next.next=Node(60)
# head.next.next.next.next.next.next=Node(70)
print(nth_node_end(head,3))

#Constraints:
#Time Complexity:O(n) 
#Aucilary space-O(1)