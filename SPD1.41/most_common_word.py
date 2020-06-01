#  Given string containing long string, find most commonly occuring word as well as its count 


# Historgram
def most_common_word(arr):
  histogram = {}
  # create histogram 
  for word in arr.split():
    if word in histogram:
      histogram[word] +=1
    else:
      histogram[word] = 1
  # find most occuring word
  most_common_word = max(histogram, key = histogram.get)
 print(most_common_word)
 
  

# Using .count()
def common_word_count(arr):
  word_frequency = []
  for word in arr.split():
    word_frequency.append(word + ":" + str(arr.count(word)))
  return word_frequency


arr = "I am walking on sunshine . The sunshine is so pretty, I love the sunshine so much"
print(most_common_word(arr))
# print(common_word_count(arr))