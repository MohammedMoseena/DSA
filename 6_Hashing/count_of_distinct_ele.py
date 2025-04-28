#Count of distinct elements in a list
def count_distinct_element(arr):
  # s=set()
  # for item in arr:
  #   s.add(item)
  # return len(s)
  return len(set(arr))
arr = [10,20,30]
print(count_distinct_element(arr))

#Constraints:
#Time complexity:O(n)
#Auxilary Space: O(n)