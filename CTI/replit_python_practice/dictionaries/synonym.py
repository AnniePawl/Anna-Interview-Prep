# Given pairs of words, return a specific word's pair 

def synonym(word_dict, word):
  return word_dict[word]

word_dict = {"Hello":"Hi", "Bye":"Goodbye", "List":"Array"}
word = "Bye"
print(synonym(word_dict, word))

# Turn input into dictionay and do same as above 
# My brute force sulution that took forever 
a = int(input()) # number of entries (key,value pairs)
my_dict = {}
data = []
for i in range(a):
  data.append(input().split())
for item in data:
  my_dict[item[0]] = item[1]
# print(my_dict)

target = input()

if target in my_dict.keys():
  print(my_dict[target])
else:
  for key, value in my_dict.items():
    if value == target:
      print(key)


# CTI SOLUTION 
# This strategy makes every input value a key AND a value
synonyms = {}
for i in range(int(input())):
  w1,w2 = input().split()
  synonyms[w1] = w2
  synonyms[w2] = w1
print(synonyms[input()])


# Turn input into dictionay and do same as above 
# My brute force sulution that took forever 
a = int(input()) # number of entries (key,value pairs)
my_dict = {}
data = []
for i in range(a):
  data.append(input().split())
for item in data:
  my_dict[item[0]] = item[1]
# print(my_dict)

target = input()

if target in my_dict.keys():
  print(my_dict[target])
else:
  for key, value in my_dict.items():
    if value == target:
      print(key)
