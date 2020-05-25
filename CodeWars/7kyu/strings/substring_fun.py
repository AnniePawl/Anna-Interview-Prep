# Given array of words, concatenate nth letter of each word. N is position of word in list 

def concatenate(words):
  new_string = ""
  index = 0
  for word in words:
    new_string += word[index]
    index += 1
  return new_string

# Using enumerate
def concatenate2(words):
  result = ""
  for index, word in enumerate(words):
    result += word[index]
  return result 

# One-liner
def concatenate3(words):
  return "".join(word[i] for i, word in enumerate(words))



print(concatenate(["yoda", "best", "has"])) # yes
print(concatenate2(["yoda", "best", "has"])) # yes
print(concatenate3(["yoda", "best", "has"])) # yes