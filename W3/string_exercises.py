s = "I do Not like Green eggs and Ham"
s2 = 'how Now brown Cow'

# 1. Find len of string 
def length(s):
  return len(s)

print(length(s)) # 32

# 2. Find frequency of all chars in a string 
def char_frequency(s):
  frequencies = {}
  s = s.lower()
  s = s.replace(' ', '')
  for char in s:
    if char in frequencies:
      frequencies[char] +=1
    else:
      frequencies[char] = 1
  return frequencies

print(char_frequency(s))

# 3. Return new string made of first 2 and last 2 chars of a string 
def first_last(s):
  return s[:2] + s [-2:]

print(first_last('butternut')) # buut

# 4. Return a string where all occurances of it's first char are changed to '$' except first char 
def cash(s):
  s = s[0] + s[1:].replace('r','$')
  return s
  
print(cash('restart reboot')) #resta$t $eboot

# 5. Turn two strings into single string seprated by space w/ first char of each string swapped 
def combine_swap(s1,s2):
  s3 = s2[0] + s1[1:] + ' ' + s1[0] + s2[1:]
  return s3

print(combine_swap('abc', 'xyz')) # xbc ayz