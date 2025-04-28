#Array Implementation of Queue
class Queue:
  def __init__(self,c):
    self.capacity=c
    self.queue=[]
    self.front=self.rear=0
  def Enqueue(self,data):
    if (self.capacity==self.rear):
      print("\nQueue is full")
    else:
      self.queue.append(data)
      self.rear+=1
  def Dequeue(self):
    if (self.front==self.rear):
      print("\nQueue is empty")
    else:
      self.queue.pop(0)
      self.rear-=1
  def Display(self):
    if (self.front==self.rear):
      print("\nQueue is empty")   
    else:
      for item in self.queue:
        print(item,'<--',end="")
      print("\n")
  def Front(self):
    if (self.front==self.rear):
      print("\nQueue is empty")   
    else:
      return self.queue[self.front]
    

q=Queue(4)
q.Display()
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
q.Enqueue(50)
q.Display()
q.Enqueue(60)
q.Display()
q.Dequeue()
q.Dequeue()
q.Display()
print(q.Front())
