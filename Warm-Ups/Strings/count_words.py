# Given a string of words, return number of words

def count_words(str):
  return sum(1 for word in str.split(" "))

print(count_words("Hello World")) # 2 
print(count_words("My name is hello kitty")) # 5

def count_words2(str):
  return len(str.split(" "))

print(count_words2("Hello World")) # 2 
print(count_words2("My name is hello kitty")) # 5

def count_words3(str):
  word_list = [word for word in str.split(" ")]
  return len(word_list)


print(count_words3("Hello World")) # 2 
print(count_words3("My name is hello kitty")) # 3