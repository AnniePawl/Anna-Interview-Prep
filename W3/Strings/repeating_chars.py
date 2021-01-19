# Find first non repeating char in string (char that only appears 1x)

def first_non_repeating(str):
  counts = {}
  # iterate over letters in str and keep track of occurances 
  for letter in str:
    if letter in counts:
      counts[letter] += 1 
    else:
      counts[letter] = 1 
  
  # iterate over counts, return first letter that only occured once 
  for letter in counts:
    if counts[letter] == 1:
      return letter 
  return 'no repearting char'
  

print(first_non_repeating('annarocks')) # r
print(first_non_repeating('anna')) # no repeating chars


# Find first repeating char in string
def first_repeating(str):
  counts = {}
  for letter in str:
    if letter in counts:
      counts[letter] += 1 
    else:
      counts[letter] = 1

  for letter in counts:
    if counts[letter] > 1:
      return letter 
  return 'no repeating chars'

print(first_repeating('anna')) # a ? 
print(first_repeating('amber')) # no letters repeat 

def first_repeating2(str):
  for i, char in enumerate(str):
    if str[i:].count(char) > 1:
      return char

print(first_repeating2('anna')) # a
print(first_repeating2('amber')) # no letters repeat 
