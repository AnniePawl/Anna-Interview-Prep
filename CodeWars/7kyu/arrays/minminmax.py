# Return [smallest, minimumAbsent, largest]
# minimumAbsent = smallest num between largest and smallest that is not in array 


def minminmax(numbers):
  mmm = []
  smallest = min(numbers)
  biggest = max(numbers)
  next_smallest = smallest + 1
  for i in range(next_smallest, biggest + 1):
    if i not in numbers:
      next_smallest = i 
      break 
  return [smallest,next_smallest,biggest]

# Using sets 
def minminmax2(numbers):
  s, mi, ma = set(numbers), min(numbers), max(numbers)
  return [mi, next(x for x in range(mi+1, ma) if x not in s), ma]

print(minminmax([1, 3, -3, -2, 8, -1])) # [-3, 0, 8]
print(minminmax([-1, 4, 5, -23, 24])) # [-23,-22,24]

print(minminmax2([1, 3, -3, -2, 8, -1])) # [-3, 0, 8]
print(minminmax2([-1, 4, 5, -23, 24])) # [-23,-22,24]

