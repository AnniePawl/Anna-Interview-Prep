# Create a function that sorts a dictionary by value 
import string 


# Inefficient Solution 
def anagram(s):
  i = 0 
  j = len(s)-1
  while i < j:
    while not s[i].isalnum():
      i +=1 
    while not s[j].isalnum():
      j -=1

    if s[i] != s[j]:
      return False 
    
    i +=1
    j -=1
  
  return True 

print(anagram("raCE: car"))  # True 

