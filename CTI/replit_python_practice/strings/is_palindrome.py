# Given a string, return True if it's a palindrome 
# Palindrome--> word/ phrease read same backward and forward 
# Example --> "racecar"
# Example --> "Race Car!!"? Caps?, Whitespaces? Punctuation?
import string 

def is_palindrome(s):
  pass
  s = s.replace(" ","")# remove whitespaces 
  s = s.lower()# make letters lowercase 
  s = s.translate(str.maketrans("","",string.punctuation))# remove punctuation
  # check if word same backward 
  return s == s[::-1]

# print(is_palindrome("racecar")) # True
# print(is_palindrome("Race Car!!")) # True
# print(is_palindrome("butter")) # False



def is_palindrome2(s):
# Create 2 pointers one starting at beginning and one at end 
  i = 0 
  j = len(s)-1
  # Keep going until reach middle of
  while i < j:
# Ignore/ move pointers if punctuation or capital 
    while not s[i].isalpha():
      i+=1
    while not s[j].isalpha():
      j -= 1
    
# If corresponding chars aren't same:
    if s[i].lower() != s[j].lower():
      return False
    
    i+=1
    j-=1

  return True

print(is_palindrome2("racecar")) # True
print(is_palindrome2("Race Car!!")) # True
print(is_palindrome2("butter")) # False


Given a string, return True is string a palindrome 
Palindrome -> read same backwards and fowards
Example: "racecar"
Example: "Race Car!!" --> punctuation, whitespace, capital letters


import string

def is_palindrome(s):
  s = s.replace(" ","")# Remove whitespace 
  s = s.lower()# Make letters lowercase 
  # Remove punctuation 
  s = s.translate(str.maketrans('','',string.punctuation))
  # If word is spelled same backwards and fowards
  return s == s[::-1]
  
print(is_palindrome("racecar")) # True
print(is_palindrome("Race Car!!")) # True
print(is_palindrome("butter")) # False

def is_palindrome2(s):
  # Create 2 pointers . One traverses forward, one traverses backwards
  i = 0
  j =len(s)-1
  while i < j:
    while not s[i].isalpha():
      i +=1
    while not s[j].isalpha():
      j-=1
    # Check if char is letter. Otherwise, move pointer along 
    if s[i].lower() != s[j].lower():
      return False
  # Check if corresponding letters match. If not, return False 
  # Otherwise, move pointer along 
    i +=1
    j -=1
  return True
  # If make it to middle, return True

print(is_palindrome2("racecar")) # True
print(is_palindrome2("Race Car!!")) # True
print(is_palindrome2("butter")) # False
