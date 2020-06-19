# Count occurances of each char that appears in a string 

def count_occurances(str):
  letter_count = {}
  for letter in str.lower():
    if letter in letter_count:
      letter_count[letter] +=1
    else: 
      letter_count[letter] =1
  return letter_count
  

def count_occurances2(str):
  countDict = dict()
  for char in str.lower():
    count = str.count(char)
    countDict[char] = count 
  return countDict

print(count_occurances("Anna")) # {"a":2, "n":2}
print(count_occurances("bob")) # {"b":2 , "o":1}


print(count_occurances2("Anna")) # {"a":2, "n":2}
print(count_occurances2("bob")) # {"b":2 , "o":1}

# Extra Practice 
def count_lower_upper(str):
  lower_count = 0
  upper_count = 0
  for letter in str:
    if letter.islower():
      lower_count +=1 
    else:
      upper_count +=1
  return lower_count, upper_count

print(count_lower_upper("BoringAppleSeed")) # (12,3)


def letter_histogram(str):
  letter_dict = dict()
  # could also be written as .... letter_dict = dict{}
  for letter in str:
    if letter in letter_dict:
      letter_dict[letter] +=1
    else:
      letter_dict[letter] = 1
  return letter_dict

print(letter_histogram("annabanana")) # {a:5, n:4, b:1}