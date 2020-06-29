# Given two strings, determine if they're anagrams 


# Using sorted 
# O(n log n) ?
def valid_anagrams(s,t):
  if sorted(s) == sorted(t):
    return True 
  return False

print(valid_anagrams('lap','alp')) #True
print(valid_anagrams('lark','larp')) #False

# Without Sort
# .count() time complexity = O(n)
def valid_anagrams2(s,t):
  for letter in s:
    if s.count(letter) != t.count(letter):
      return False 
  return True


print(valid_anagrams2('lap','alp')) #True
print(valid_anagrams2('lark','larp')) #False