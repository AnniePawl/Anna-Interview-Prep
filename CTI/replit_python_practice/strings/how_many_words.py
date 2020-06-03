# Given string separated by spaces, return how many words there are 


def word_count(str):
  return len(str.split(" "))

print(word_count("Hello World")) # 2
print(word_count("Bye Bye Birdie")) # 3