#Reverse words of string
#Method-1
def rev_word_of_str(s):
  return " ".join((s.split(" "))[::-1])

s="Welcome to dsa"
print(rev_word_of_str(s))