# Given pairs of words, return a specific word's pair 

def synonym(word_dict, word):
  return word_dict[word]

word_dict = {"Hello":"Hi", "Bye":"Goodbye", "List":"Array"}
word = "Bye"

print(synonym(word_dict, word))

# Turn input into dictionay and do same as above 
def synonym2():
  dict = {}
  i = 2
  s = [s for s in input().split(" ")]
  for word in s[:-1:2]:
    dict[word] = s[i]
    i+=2
  return dict

print(synonym2())
