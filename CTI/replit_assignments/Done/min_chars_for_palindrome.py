# Given a string, only operation allowed is insert chars at beginning of string 
# Return num of chars needed to make string a palindrom 

# Strategy - remove letters from string until empty or palindrome 
def min_chars_del(chars):
  chars = list(chars)
  count = 0 
  while len(chars) > 0 :
    if chars == chars[::-1]:
      return count
    else:
      chars.pop()
      count +=1

def is_palindrome(chars):
  return chars == chars[::-1]

def min_chars_insert(chars):
  insertions = 0
  while not is_palindrome(chars) and len(chars) >1:
    chars = chars[0:-1]
    insertions +=1
  return insertions
 


# Del Approach
print(min_chars_del("ABA")) # 0
print(min_chars_del("AB")) # 1
print(min_chars_del("ABC")) # 2
print(min_chars_del("AACECAAAA")) # 2

# Insert Approach 
print("insert approach")
print(min_chars_insert("ABA")) # 0
print(min_chars_insert("AB")) # 1
print(min_chars_insert("ABC")) # 2
print(min_chars_insert("AACECAAAA")) # 2


