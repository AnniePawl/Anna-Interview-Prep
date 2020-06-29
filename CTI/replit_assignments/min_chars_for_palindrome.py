# Given a string, only operation allowed is insert chars at beginning of string 
# Return num of chars needed to make string a palindrom 

def is_palindrome(chars):
  if chars == chars[::-1]:
    return True

def min_chars(chars):
  
  while not is_palindrome():



print(min_chars("ABA")) # 0
print(min_chars("AB")) # 1
print(min_chars("ABC")) # 2
print(min_chars("AACECAAAA")) # 2