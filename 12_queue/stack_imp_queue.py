#Implementation of stack using queue
from collections import deque
class Stack:
  def __init__(self):
    self.q1=deque()
    self.q2=deque()
  def push(self,x):
    self.q2.append(x)
    while self.q1:
      self.q2.append(self.q1.popleft())
    self.q1,self.q2=self.q2,self.q1
  def pop(self):
    if self.q1:
      return self.q1.popleft()
    return None
  def top(self):
    if self.q1:
      return self.q1[0]
    else:
      return 0
  def size(self):
    return len(self.q1)
q=Stack()
q.push(30)
q.push(20)
q.push(10)
q.push(40)
q.pop()
print(q.top())
print(q.q1)

#Constraints:
#Time complexity:O(n)
#Auxilary Space:O(1)