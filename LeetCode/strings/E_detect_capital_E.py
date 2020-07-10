# Given word, return True if :
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".


def detect_capital(word):
  if word.islower() or word.isupper() or word.istitle():
    return True 
  else:
    return False

print(detect_capital("USA")) # True 
print(detect_capital("google")) # True 
print(detect_capital("Anna")) # True 
print(detect_capital("AnA")) # False