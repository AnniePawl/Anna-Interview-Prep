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


