#  67. Remove consecutive duplicates from string 
def remove_consecutive_duplicates(str):
  str = list(str)
  j = 0
  for i in range(len(str)):
    if str[j] != str[i]:
      j += 1
      str[j] = str[i]

  j +=1
  str = str[:j]
  return ''.join(str)
 
def remove_consecutive_duplicates2(str):
  seen = str[0]
  result = str[0]
  for char in str[1:]:
    if char != seen:
      result += char 
      seen = char
  return result


def remove_consecutive_duplicates3(str):
  return ''.join(([v for i, v in enumerate(str) if i == 0 or v != str[i-1]]))

  

# Consider if duplicates at beginning and end of string
print(remove_consecutive_duplicates('annna')) # ana
print(remove_consecutive_duplicates('blahhh')) # blah
print(remove_consecutive_duplicates('aaron')) # aron
print(remove_consecutive_duplicates('root beer')) # rot ber



print(remove_consecutive_duplicates2('annna')) # ana
print(remove_consecutive_duplicates2('blahhh')) # blah
print(remove_consecutive_duplicates2('aaron')) # aron
print(remove_consecutive_duplicates2('root beer')) # rot ber



print(remove_consecutive_duplicates3('annna')) # ana
print(remove_consecutive_duplicates3('blahhh')) # blah
print(remove_consecutive_duplicates3('aaron')) # aron
print(remove_consecutive_duplicates3('root beer')) # rot ber

# Using Recursion : 

