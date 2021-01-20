# Return max occuring char in a string 

def max_occuring(str):
  counts = {}
  for letter in str.replace(' ', ''):
    if letter in counts:
      counts[letter] += 1 
    else:
      counts[letter] = 1
  
  return max(counts, key=counts.get)


print(max_occuring('hansel and gretel'))