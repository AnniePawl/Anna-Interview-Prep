# Given 2 arrays, mash them together so new array has alternating elements 

def array_mash(a,b):
  new_array = a
  i = 1
  for item in b:
    new_array.insert(i, item)
    i +=2
  return new_array

  # Using zip?
  def array_mash(xs, ys):
    return [z for p in zip(xs, ys) for z in p]


print(array_mash([1,2,3], ['a','b','c'])) # [1,'a',2,'b',3,'c']