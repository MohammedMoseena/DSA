# One Odd Occurring
# Bitwise XOR operation
'''
The XOR (exclusive OR) operation is a bitwise operator that operates on binary digits. The result of XOR is 1 if the number of 1s in the bits being compared is odd

In simpler terms:

If the bits are the same (both 0s or both 1s), the result is 0.
If the bits are different (one is 0 and the other is 1), the result is 1.

Properties of XOR

1. XOR of a number with itself is 0: 
a⊕a=0

2. XOR of a number with 0 is the number itself: 
a⊕0=a
'''

def one_odd(l):
  res=0
  for i in range(0,len(l)):
    res=res^(l[i])
  return res
l=[1,2,3,2,3,1,3]  
# l=[5,7,2,7,5,2,5]
print(one_odd(l))