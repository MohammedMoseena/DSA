#Implementation of chaining using in python
class MyHash:
  def __init__(self,size,arr=None):
    self.size=size
    self.arr=[[] for i in range(size)]
  def insert(self,element):
    index=element%(self.size)
    (self.arr[index]).append(element)
  def search(self,element):
    index=element%(self.size)
    return element in self.arr[index]
  def remove(self,element):
    index=element%(self.size)
    if element in self.arr[index]:
      self.arr[index].remove(element)

h=MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
h.remove(56)
print(h.arr)



