# Average or Mean of a list
'''
1. len() function takes time complexity O(1).This is because the length of a list in Python is stored as an attribute of the list object. When you call len(), it simply returns this pre-stored value without needing to traverse the list or perform any additional calculations. 

2. The sum() function in Python, which is used to find the sum of the elements in a list, has a time complexity of O(n)

This is because the sum() function iterates through each element of the list exactly once, adding each element to a running total. As a result, the time it takes to compute the sum grows linearly with the number of elements in the list.
'''
import math
def average_list(l):
  return round(sum(l)/len(l),2)
l=[10,20,30,40]
print(average_list(l))

#Constraints
#Time complexity:O(n)
#Space complexity:O(1)
#Auxilary Space:O(1)
