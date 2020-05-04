# Return True if input string is an isogram (no repeating letters, consecutive or non-consecutive). Ignore letter case and assume empty string is isogram 


def is_isogram(string):
  # make everything lowercase 
  lower_string = string.lower()
  # append letters to list 
  letter_list = []
  for letter in lower_string:
    if letter in letter_list:
      return False 
    else: letter_list.append(letter)
  return True


# Using .count()
  def is_isogram_v2(string):
    string = string.lower()
    for letter in string:
      if string.count(letter) >1: 
        return False 
    return True

# Most concise 
def is_isogram_v3(string):
  return len(string) == len(set(string.lower()))

  

print(is_isogram('aba'))  # False
print(is_isogram('abC'))  # True 
print(is_isogram('isIsogram'))  # False 
print(is_isogram(''))  # True 
print("V2 w/ .count()")
print(is_isogram('aba'))  # False
print(is_isogram('abC'))  # True 
print(is_isogram('isIsogram'))  # False 
print(is_isogram(''))  # True 
print("V3 using set")
print(is_isogram('aba'))  # False
print(is_isogram('abC'))  # True 
print(is_isogram('isIsogram'))  # False 
print(is_isogram(''))  # True 
