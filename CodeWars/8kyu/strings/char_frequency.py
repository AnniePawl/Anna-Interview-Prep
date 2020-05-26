# Return frequency of each character in string
from collections import Counter 

def frequency(str):
  count = {}
  for letter in str:
    if letter in count:
      count[letter] +=1
    else:
      count[letter] = 1
  return count

def frequency2(str):
  return Counter(str)

def frequency3(str):
  result = {}
  for letter in str:
    result[letter] = result.get(letter,0) +1
  return result


print(frequency("doob")) # {"d":1, "o":2,"b":1}
print(frequency2("boob")) # {"d":1, "o":2,"b":1}
print(frequency3("cat")) # {"d":1, "o":2,"b":1}