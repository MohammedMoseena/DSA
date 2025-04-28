#Implementation of Open Addressing
#-1 signifies cell is empty
#-2 signies element is deleted from cell
class MyHash:
  def __init__(self,cap):
    self.cap=cap
    self.arr=[-1 for i in range(self.cap)]
    self.size=0
  
  def hash(self,element):
    return element%(self.cap)
  
  def search(self,element):
    temp=self.arr
    index=self.hash(element)
    i=index
    while temp[i]!=-1:
      if temp[i]==element: #Item found
        return True
      i = (i+1)%(self.cap)
      if i==h: #Whole list is filled but item not found
        return False
    return False #Whenever empty slot is encountered

  def insert(self,element):
    if self.size==self.cap: #When list is fully occupied
      return True
    if self.search(element): #Already element is present
      return False
    
    temp=self.arr
    index=self.hash(element)
    while temp[index] not in (-1,-2):
        index=(index+1)%(self.cap)
    temp[index]=element
    self.size+=1
    self.arr=temp
    return True

  def remove(self,element):
    index=self.hash(element)
    temp=self.arr
    i=index
    while temp[i]!=-1:
      if temp[i]==element:
        temp[i]=-2
        return True
      i=(i+1)%(self.cap)
      if i==h:
        return False
    return False
      
 

h=MyHash(7)
print("Initially",h.arr)
h.insert(49)
h.insert(56)
h.insert(72)
print("After Insertions",h.arr)
print(h.search(56))
h.remove(56)
print("After Removal",h.arr)
print(h.search(56))