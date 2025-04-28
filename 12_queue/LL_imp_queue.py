#Linked List Implementation of Queue in Python
#maintain head and tail nodes to execute queue operations in O(1)
#Using Single Linked List we can set only in this way rear-tail node and front-head node but not vice versa
#In single linked list in O(1) time we can perform all general queue operations(enque,deque,size,isempty,getfront,getrare) only when we add from rear end remove from front endL

class Node():
  #Node creation
  def __init__(self,data):
    self.key=data
    self.next=None

class MyQueue():
  #Initialization
  def __init__(self):
    self.front=None
    self.rear=None
    self.size=0

  #IsEmpty Operation
  def isEmpty(self):
    if self.front==None:
      return True
    return False
  
  #Print Linked List
  def printLL(self):
    curr=self.front
    while curr!=None:
      print(curr.key,end=" ")
      curr=curr.next
    print('\n')
  
  #Enque Operation
  def enque(self,data):
    newnode=Node(data)
    if self.front==None:
      self.front=newnode
      self.rear=self.front
      self.size+=1
    else:
      self.rear.next=newnode
      self.rear=self.rear.next
      self.size+=1
  
  #Deque Operation
  def deque(self):
    if self.front==None:
      return None
    temp=self.front
    self.front=self.front.next
    temp.next=None
    self.size-=1
  
  #Size Operation
  def sizeLL(self):
    return self.size

  #getFront Opeartion
  def getFront(self):
    if self.front==None:
      return None
    return self.front.key
  
  #getRear Opeartion
  def getRear(self):
    if self.rear==None:
      return None
    else:
      return self.rear.key

q=MyQueue()
q.enque(10)
q.printLL()
q.enque(20)
q.printLL()
q.enque(30)
q.printLL()
q.deque()
q.printLL()
print(q.sizeLL())
q.enque(40)
q.printLL()
print(q.getFront())
print(q.getRear())
print(q.isEmpty())
  
#Constraints
#Time Complexity: O(1)
#Auxilary Space:O(n)
