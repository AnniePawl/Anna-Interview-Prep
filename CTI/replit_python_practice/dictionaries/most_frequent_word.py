# Given int of number of input lines, followed by lines of words, print word that occurs most often 
# If multiple words occur same amount, print first in alphabetical order

words_histo = {}
for i in range(int(input())):
  words = input().split()
  # Check if word in dict 
  for word in words:
    if word in words_histo:
      words_histo[word] +=1
    else:
      words_histo[word] = 1
# print(words_histo)

max_value = max(words_histo.values())
max_keys = []
for key in words_histo.keys():
  if words_histo[key] == max_value:
    max_keys.append(key)

print(sorted(max_keys)[0])


# CTI Solution 
words_count = {}
for i in range(int(input())):
  words = input().split()
  for word in words:
    if word not in words_count:
      words_count[word] = 0
    words_count[word] += 1
max_frequency = max(words_count.values())
for word in sorted(words_count):
  if words_count[word] == max_frequency:
    print(word)
    break


# Sample Input 
# 2
# apple orange banana
# banana orange

# Sample output : banana 