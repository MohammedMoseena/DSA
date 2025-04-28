#Check for Balanced Parenthesis
def check_balanced_parenthesis(s):
  l=[]
  for item in s:
    if item in ('(','{','['):  #Opening brackets store it in stack
      l.append(item)
    else:
      if l==[]:
        return False
      elif (item==')' and l[-1]=='(') or (item==']' and l[-1]=='[') or (item=='{' and l[-1]=='}'):
        l.pop()
      else:
        return False
  if l==[]:
    return True
  else:
    return False


s=input("Enter the input: ")
print(check_balanced_parenthesis(s))

#Constraints
#Time Complexity:O(n)
#Auxilary Space:O(n)