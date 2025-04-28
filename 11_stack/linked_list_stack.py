#Linked list implementation of stack in python
class Node:
  def __init__(self,key):
    self.data=key 
    self.next=None

class Mystack():
  def __init__(self):
    self.head=None
    self.size=0

  def push(self,key):
    temp=Node(key)
    temp.next=self.head
    self.head=temp
    self.size=self.size+1
  
  def pop(self):
    if self.head==None:
      return None
    self.head=self.head.next
    self.size=self.size-1
    return self.head
  
  def size(self):
    return self.size
  
  def peek(self):
    if self.head==None:
      return None
    return self.head.data
  
  def printll(self):
    curr=self.head
    while curr!=None:
      print(curr.data,end=" ")
      curr=curr.next
  

s=Mystack()
s.push(10)
s.push(20)
s.push(30)
s.printll()
print('\n')
print(s.pop())
s.printll()
print('\n')
print(s.peek())

    
