#Frequency of each distinct item in an array
def frequency(arr):
  count_dict=dict()
  for item in arr:
    if item in count_dict.keys():
      count_dict[item]+=1
    else:
      count_dict[item]=1
  for key,value in count_dict.items():
    print(f"{key} {value}")

arr=[10,20]
frequency(arr)

#constraints:
#Time complexity:O(n) - 2 traversals
#Auxilary Space:O(n)