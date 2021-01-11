# Find and return words that contain both letters and numbers 
# Use built-in any() which return T if any iterable = T

def letter_digit(s):
  result = []
  s = s.split(' ')
  for word in s:
    if any(letter.isdigit() for letter in word) and any( letter.isalpha() for letter in word):
      result.append(word)
  return '\n'.join(result)

print(letter_digit("Emma25 is Data scientist50 and AI Expert"))
# Emma25
# scientist50