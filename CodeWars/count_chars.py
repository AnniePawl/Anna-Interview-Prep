# Count all the occurring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }
from collections import Counter 

def count_occurances(string):
  occurances = {}
  for letter in string:
    if letter in occurances:
      occurances[letter] +=1
    else:
      occurances[letter] =1 
  return occurances

def count_occurances_v2(string):
  return Counter(string)

print(count_occurances('a,a,b,c,d,d,e'))
print(count_occurances_v2('a,a,b,c,d,d,e'))