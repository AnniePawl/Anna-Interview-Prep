#  Given a list of words, return new list with len of each word after space 

def add_len(words):
  new_array = []
  split =  words.split()
  for word in split:
    new_array.append( word + " " + str(len(word)))
  return new_array
   

def add_len2(words):
  return [word + " " + str(len(word)) for word in words.split()]


print(add_len("hello world")) # ["hello 5, world 5"]
print(add_len("boy scout club")) # ["boy 3, scout 5, club 4"]

print(add_len2("Anna Pawl")) # ['anna 4', 'pawl 4']