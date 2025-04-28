# Remove Duplicates from a Sorted list
class Node:
  def __init__(self,key):
    self.key=key
    self.next=None
def printlinkedlist(head):
  while head!=None:
    print(head.key,end=" ")
    head=head.next
def remove_duplicates_from_sorted_list(head):
  if (head==None) or (head.next==None):
    return head
  else:
    curr=head
    while head.next!=None:
      if head.key==head.next.key:
        head.next=head.next.next
      else:
        head=head.next

    head=curr
    return head
    
    

head=Node(10)
head.next=Node(20)
head.next.next=Node(20)
head.next.next.next=Node(30)
head.next.next.next.next=Node(30)
head.next.next.next.next.next=Node(30)
head=remove_duplicates_from_sorted_list(head)
printlinkedlist(head)

#Constraints:
#Time Complexity:O(n)
#Aucilary Space:O(1)