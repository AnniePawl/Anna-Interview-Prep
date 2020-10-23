# Given a string, determinte if it's a palindrome 
# Palindrome --> word, phrase that reads same backward and forward 

# Examples --> eye, Anna, Race car, Madam, I'm Adam 

# First Approach 
# make letters lowercase 
# remove whitespace 
# remove punctuation 
# check if word spelled same back to front 
import string 

# string immutable --> string methods are creating new strings --> extra space 
def palindrome(s):
  s = s.lower()
  s = s.replace(" ","")
  s = s.translate(str.maketrans("","", string.punctuation))
  return s == s[::-1]

print(palindrome("race: Car"))  # True
print(palindrome("joey"))  # False

# Second Approach (using pointers)
# initialize two pointers (i,j)
# while pointers haven't havnt overlapped:
  # check if im at an actual letter
    # if not, increment and decrement pointers
  # check if lowercased letters at i and j are same
    # if not, return False 
  # move i and j along 

# made it through , return True 
# Time Complexity = O(n)
# No extra space! 

def is_palindrome(s):
  i = 0
  j = len(s)-1
  while i < j:
    while not s[i].isalpha():
      i +=1
    while not s[j].isalpha():
      j -=1
    if s[i] !=s[j]:
      return False 
    i +=1
    j -=j
  return True
  
print(is_palindrome("race: Car"))  # True
print(is_palindrome("joey"))  # False