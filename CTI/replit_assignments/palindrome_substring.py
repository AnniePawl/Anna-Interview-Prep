# Given string, return longest palinndromic substring. 
# O(n)

def palindrome_substring(s):



print(palindrome_substring("babad")) #bab, or aba 
print(palindrome_substring("cbbd")) #bb


# Brute Force - two for loops - one traversing forward and one backwards
# Time complexity O(n^2) ?  not good...
def palindrome_substring_brute(str):
  result  = " "
  for i in range(len(str)):
    for j in range(len(str), i, -1):
      if str[i:j] ==  str[i:j][::-1]:
        if len(result) < len((str[i:j])):
          result = str[i:j]
  return result


print(palindrome_substring_brute("babad")) #bab, or aba 
print(palindrome_substring_brute("cbbd")) #bb
