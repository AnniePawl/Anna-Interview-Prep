# Given 2 strings, determine if they are anagrams. 

# Questions: 
# - What characters are we dealing with? Caps/ lowercase, spaces, punctuation?

def anagram(s1,s2):
  # Make sure letters are lowercase and remove spaces
  # Turn into array b/c strings immutable 
  s1 = [x for x in s1.lower().replace(" ","")]
  s2 = [x for x in s2.lower().replace(" ","")]

  # Create dictionaries to count occurances of each letter 
  s1_dict = {}
  s2_dict = {}
  for letter in s1:
    if letter not in s1_dict:
      s1_dict[letter] = 1
    else:
      s1_dict[letter] +=1

  for letter in s2:
    if letter not in s2_dict:
      s2_dict[letter] = 1 
    else:
      s2_dict[letter] +=1

  # Return True if the dicts are equal 
  return s1_dict == s2_dict
  



print(anagram("Listen", "silent")) # True 
print(anagram("funeral", "real fun")) # True 
print(anagram("astronomer", "moon Starer")) # True 
print(anagram("butter", "gross")) # False 
print(anagram("snot", "toss")) # False 