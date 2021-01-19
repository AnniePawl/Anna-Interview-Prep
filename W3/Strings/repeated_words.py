#  Find first repeated word in string 

def first_repeated(str):
  temp = set()
  temp = []
  for word in str.split(' '):
    if word in temp:
      return word
    else:
      temp.append(word)


print(first_repeated('ab ca bc ab')) # ab 
print(first_repeated('ab ca bc ca ab')) # ca


# Second most repeated word in string 
def second_repeated(str):
  counts = {}
  for word in str.split(' '):
    if word in counts:
      counts[word] += 1 
    else:
       counts[word] = 1 

  # sort dictionary (cant sort in place, creating new dict)
  counts2 = sorted(counts.items(), key=lambda kv: kv[1])
  return counts2[-2][0]

  
  

print(second_repeated('ab ab ba ba ba ca')) # ab