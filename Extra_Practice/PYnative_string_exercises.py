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


print(count_chars("P@#yn26at^&i5ve"))

# 6. Given two strings, created mixed string 
# first char of s1, then the last char of s2...char. leftover chars at end of result

def mixed_string(s1,s2):
  mixed_str = ""
  s2 = s2[::-1]
  for

print(mixed_string('Abc', 'Xyz')) # AzbycX


