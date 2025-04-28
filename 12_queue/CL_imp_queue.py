#Queue Implementation of circular list(cache friendly, deque & enque in O(1))
#Memory Efficient 
class MyQueue():
  def __init__(self,cap):
    self.cap=cap
    self.queue=[None]*(cap)
    self.front=0
    self.size=0

  def isEmpty(self):
    return (self.size==0)
  
  def enque(self,data):
    rear=(self.front+self.size-1)%(self.cap)
    rear=(rear+1)%(self.cap)
    self.queue[(rear)]=data
    self.size+=1


  def deque(self):
    if self.size==0:
      return None
    popped=self.queue[(self.front)]
    self.queue[(self.front)]=None
    self.front=(self.front+1)%(self.cap)
    self.size-=1
    return popped
  
  def getFront(self):
    if self.size==0:
      return None
    return self.queue[(self.front)]
  
  def getrear(self):
    if self.size==0:
      return None
    rear=(self.front+self.size-1)%(self.cap)
    return self.queue[(rear)]

q=MyQueue(5)
q.enque(10)
q.enque(20)
q.enque(30)
print(q.queue)
print(q.deque())
print(q.queue)
print(q.size)
q.enque(40)
print(q.queue)
print(q.getFront())
print(q.getrear())
print(q.isEmpty())


#Constraints
#Time complexity:O(1)
#Auxilary Space:O(n)