# Find second most repeated word in a string 

def second_repeated(str):
  counts = {}
  for word in str.split():
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1 
    
  return sorted(counts, key= lambda kv:kv[1])[-2]
  # Line below gets key with max value
  # return max(counts, key=counts.get)


print(second_repeated('ab ba ba ab ba cd')) # ab