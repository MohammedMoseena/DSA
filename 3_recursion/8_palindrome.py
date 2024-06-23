#Palindrome check using recursive function

def palindrome(str,start,end):
  if start>=end:
    return True
  return ( (str[start]==str[end]) and (palindrome(str,start+1,end-1)) )
  
str=input("Enter: ")
print(palindrome(str,0,len(str)-1))

