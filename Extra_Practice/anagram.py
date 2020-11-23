# # Given 2 string, return True is they are anagrams 
# # Anagrams are words/ phrases formed by rearranginng letters 
# # Example --> 'listen', 'silent' 
# # 'Astromer!', 'Moon STARER' --> Spaces? Caps ? Punctuation ?

# # Time Complexity --> O(n)
# # Space Complexity --> O(n)
# def anagram(s1,s2):
#   letters = {}
#   # Create historgram for letters in S1
#   for letter in s1:
#     if letter.lower() in letters:
#       letters[letter.lower()] +=1
#     else:
#       letters[letter.lower()] =1
    
#   #Iterate over lettes in S2
#   for letter in s2:
#     if letter.lower() in letters:
#        # Decrement value in letter dict if letter seen 
#       letters[letter.lower()] -=1
#     else:
#       letters[letter.lower()]= 1
#   # print(letters)
 
#   # If dict values all == 0: anagram! 
#   for key in letters.keys():
#     if letters[key] != 0:
#       return False 
#   return True
  

# print(anagram("Listen", "silent")) # True 
# print(anagram("funeral", "real fun")) # True 
# # print(anagram("Astronomer", "moon Starer")) # True 
# # print(anagram("butter", "gross")) # False 
# # print(anagram("snot", "toss")) # False 


# Given 2 string, determine whether they are anagrams 
# Anagrams --> words/ phrases spelled by rearranging characters 
# Example --> "listen", "silent"

# Time Complexity 0(n)
# Space Complexity 
def anagram(s1,s2):
  s1 = s1.lower().replace(" ","") # O(2n)
  s2 = s2.lower().replace(" ","") # O(2n)
  letters = {}
  # Iterate over chars in S1 and create historgram 
  for letter in s1: # O(n)
    if letter in letters:
      letters[letter] +=1
    else:
      letters[letter] =1
  
  # Iterate over chars in S2 - and decremnt values if letter seen 
  for letter in s2: #O(n)
    if letter in letters:
      letters[letter] -=1
    else:
      letters[letter] =1
  print(letters)

  # If all dict values == 0:
    # anagram! 
  for key in letters.keys(): # O(n)
    if letters[key] !=0:
      return False 
  
  return True


print(anagram("listen", "silent")) # True 
print(anagram("Astronomer", 'moon Starer')) # True