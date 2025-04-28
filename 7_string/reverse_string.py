#Reverse the string
#Method-1: arr[::-1]
def reverse_string(arr):
  rev=""
  for item in arr:
    rev= item+rev
  return rev
arr="abcd"
print(reverse_string(arr))

#Constarints
#Time complexity:O(n)
#Auxilary Space:O(n)