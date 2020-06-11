# Given string, return longest palinndromic substring. 

def palindrome_substring(str):
  substring = ""
  left = 0 
  right = len(str)-1
  if str(left) == str(right):
    

print(palindrome_substring("babad")) #bab, or aba 
print(palindrome_substring("cbbd")) #bb
