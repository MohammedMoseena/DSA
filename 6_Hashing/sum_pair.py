# You are given an array of distinct integers and sum. Check if there's a pair with the given sum in the array

def sumpair(arr,N,sum):
  d=dict()
  for item in arr:
    if (sum-item) in d:
      return 1
    d[item]=item
  else:
    return 0

arr=[1,2,3,4,5,6,7,8,9,10]
N=10
sum=10
print(sumpair(arr,N,sum))

#Constraints
#Time complexity: O(n)
#Space complexity: O(n)