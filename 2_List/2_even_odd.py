# Seperate Even and Odd 
def even_odd(l):
  # even=[]
  # odd=[]
  # for i in range(len(l)):
  #   if l[i]%2==0:
  #     even.append(l[i])
  #   else:
  #     odd.append(l[i])
  # Using List comprehension
  #List comprehension helps us to reduce lines of code
  return [l[i] for i in range(len(l)) if l[i]%2==0],[l[i] for i in range(len(l)) if l[i]%2!=0]

l=[10,12,11,16]
even,odd=even_odd(l)
print("Even:",even)
print("Odd:",odd)  


#Time complexity:O(n)
#Space complexity:O(n)
#Auxilary space:O(1)
  