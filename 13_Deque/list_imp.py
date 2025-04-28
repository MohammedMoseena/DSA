#List Implementation of Deque

class Deque:
  def __init__(self,k):
    self.q=[None]*k
    self.cap=k
    self.front=0
    self.size=0
  
  def insertFront(self,data):
    if self.size==self.cap:
      return None
    self.front=(self.front-1)%(self.cap)
    self.q[self.front]=data
    self.size+=1

  def insertRear(self,data):
    if self.size==self.cap:
      return None
    rear=(self.front+self.size-1)%(self.cap)
    rear=(rear+1)%(self.cap)
    self.q[rear]=data
    self.size+=1

  def deleteFront(self):
    if self.size==0:
      return None
    popped=self.q[self.front]
    self.q[self.front]=None
    self.front=(self.front+1)%(self.cap)
    self.size-=1
  
  def deleteRear(self):
    if self.size==0:
      return None
    popped=self.q[self.front]
    rear=(self.front+self.size-1)%(self.cap)
    self.q[rear]=None
    rear=(rear-1)%(self.cap)
    self.size-=1

d=Deque(4)
d.insertRear(10)
print(d.q)
d.insertFront(20)
print(d.q)
d.insertFront(30)
print(d.q)
d.deleteFront()
print(d.q)
d.deleteRear()
print(d.q)

    
#Constraints:
#Time Complexity:O(1)
#Auxilary Space:O(1)