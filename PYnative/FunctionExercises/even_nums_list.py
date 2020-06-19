# Generate list of even nums 

def even_nums(max):
  evens = [ ]
  for num in range(1,max +1):
    if num % 2 == 0:
      evens.append(num)
  return evens

print(even_nums(10))
print(even_nums(30))

# List Comprehension 
def even_nums2(max):
  return [x for x in range(1,max+1) if x % 2 == 0]

print(even_nums2(10))
print(even_nums2(30))


# Print even numbers from 1-40
print(list(range(2,41,2)))