# 1. Given an off len str, return string made of middle 3 chars 

def middle_three(str):
  return str[(len(str)//2)-1:(len(str)//2)+2]

print(middle_three("jaSonAy")) #Son

# 2. Given 2 strings, create new string by appending s2 in middle of s1 
def append_middle(s1,s2):
  return s1[:len(s1)//2] + s2 + s1[len(s1)//2:]

print(append_middle('Ault', 'Kelly')) #AuKellylt

# 3. Given 2 stings, return new string made of first, middle and last char for each input
def new_string(s1,s2):
  return s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]

print(new_string("America", "Japan")) # AJrpan


# 4. Given string w/ lower and uppercase letters, arrange chars so lowercase comes first 
def sort_str(s1):
  lower = ""
  upper = ""
  for letter in s1:
    if letter.islower():
      lower += letter
    else:
      upper += letter
  return  lower + upper

def sort_str2(s1):
  lower = []
  upper = []
  for letter in s1:
    if letter.islower():
      lower.append(letter)
    else:
      upper.append(letter)
  return "".join(lower + upper)

print(sort_str("PyNaTive")) #yaivePNT
print(sort_str2("AnnaPawl")) #nnaawlAP

# 5. Count all lowercase, uppercase, digits, and special symbols in given string
# brute force
def count_chars(s1):
  chars = 0 
  digit = 0
  symbol = 0
  for letter in s1:
    if letter.isalpha():
      chars +=1
    if letter.isdigit():
      digit+=1
    else:
      symbol +=1
  print("Chars = " + str(chars) + "\n" + "Digits = " + str(digit) + "\n" + "Symbol = " + str(symbol)) 

def count_chars2(s1):
  chars = sum(1 for letter in s1 if letter.isalpha())
  digit = sum(1 for letter in s1 if letter.isdigit())
  symbol = sum(1 for letter in s1 if not letter.isalnum())
  
  return {"Chars":chars, "Digit":digit,"Symbol":symbol}


print(count_chars("P@#yn26at^&i5ve"))
print(count_chars2("P@#yn26at^&i5ve"))

# 6. Given two strings, created mixed string 
# first char of s1, then the last char of s2...char. leftover chars at end of result


# 7. Check if two strings are balance. all cahrs in s1 are in s2 

def balanced_str(s1,s2):
  return s1 in s2


def balanced_str2(s1,s2):
  for letter in s1:
    if letter in s2:
      continue
    else:
      return False 
  return True

print(balanced_str('Yn', 'PYnative')) # True
print(balanced_str('Yfn', 'PYnative')) # False

print(balanced_str2('Yn', 'PYnative')) # True
print(balanced_str2('Yfn', 'PYnative')) # False

# 8. Find all occurances of "USA" in given string, ignore case
def find_occurances(str):
  # str = str.lower()
  return str.count('usa')

print(find_occurances('welcome to USA. usa is awesome ')) # 2

# 9. Given a str, return sum of digits that appear in str, ignore all chars

def sum_average(s1):
  temp = "0"
  sum = 0 
  for char in s1:
    if char.isdigit():
      temp += char
    else:
      sum += int(temp)
      temp = "0"
  return sum + int(temp)

print(sum_average("English = 78 Science = 83 Math = 68 History = 65")) # Sum = 294 

# 10. Count occurances of all chars in a string 
def count_occurances(s1):
  occurances = {}
  for letter in s1:
    if letter in occurances:
      occurances[letter] +=1
    else:
      occurances[letter] = 1
  return occurances

print(count_occurances("apple")) #Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters

# 11. Find last position of substring 'Emma'

def substring_position(str):
  return str.rindex('Emma')

print(substring_position("Emma is a data scientist who knows Python. Emma works at google.")) # 43 (last occurance of emma starts at index 43)


# 13. Split string into substrings at hyphens
def split_string(s):
  s = s.split("-")
  return '\n'.join(s)

print(split_string('Emma-is-a-data-scientist'))
# Emma
# is
# a
# data
# scientist

# 14. Remove empty string from list of strings
def remove_empty(s):
  for name in s:
    if name == None or name == "":
      s.remove(name)
  return s

def remove_empty2(s):
  # built in function filter
  new_s = list(filter(None, s))
  return new_s


print(remove_empty(['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']))  
print(remove_empty2(['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']))  
# ['Emma', 'Jon', 'Kelly', 'Eric']

# 15. Remove special symbols & punctuation
import string 

def remove_punctuation(s):
  return s.translate(str.maketrans('', '',string.punctuation))
  
print(remove_punctuation("/*Jon is @developer & musician"))
# “Jon is developer musician”


# 16. Remove all chars except ints from string 
def remove_alpha(s):
  return ''.join([char for char in s if char.isdigit()])

print(remove_alpha('I am 27 and 10 months'))
# 2710


# 17. Find and return words w/ letters and numbers
# Use built-in any() which returns T if any item in iterable is T
def alpha_num(s):
  s = list(s.split(' '))
  result = []
  for word in s:
    if any(letter.isdigit() for letter in word) and any(letter.isalpha() for letter in word):
      result.append(word)

  return '\n'.join(result)
  
print(alpha_num('Emma25 is Data scientist50 and AI Expert'))
# Emma25
# scientist50
