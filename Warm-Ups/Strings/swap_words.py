# Given two words, swap them at space 

def swap_words(str):
  split_str =  str.split(" ") # automatically makes list
  # return split_str[::-1]
  return split_str[1] + " " + split_str[0]

print(swap_words("Hello, World!")) # World! Hello,


def swap_words2(str):
  return " ".join(str.split(" ")[::-1])
  
print(swap_words2("Hello, World!"))