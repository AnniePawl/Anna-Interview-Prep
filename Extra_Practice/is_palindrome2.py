# Given a string, return True is string is a palindrome 
# Palindrome --> word/ phrase same forward and backward 
# 'racecar' 
# 'Race Car!!!' caps? whitespace, punctuation 

# import string

# # check if word is spelled same backward and forward 
# def palindrome(s):
#   # remove whitespace 
#   s = s.replace(" ","")
#   # make letters lowercase 
#   s = s.lower()
#   # take care of punctuation
#   s = s.translate(str.maketrans('','',string.punctuation))
#   return s 
  

# print(palindrome('racecar')) # True 
# print(palindrome('Race Car!')) # False

def palindrome(s):
# use pointers that move along string (1 from front, 1 from back)
  i = 0
  j = len(s)-1
# keep moving pointers until middle is passed  OR until check two letters and not same 
# If I hit punctuation or whitespace ,keep going 
  while i < j: 
    while not s[i].isalpha():
      i +=1
    while not s[j].isalpha():
      j-=1
# make sure letters are lowercase 
# If lettes are not match:
  # return False 
    if s[i].lower() != s[j].lower():
      return False
  # Otherwise, keep moving pointers along 
    i += 1
    j -=1
# If i reach the middle of string:
  # Return True
  return True

print(palindrome('racecar')) # True 
print(palindrome('Race Car!')) # True
print(palindrome('Ian')) # False