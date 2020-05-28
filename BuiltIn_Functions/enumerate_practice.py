# enumerate(iterable, start = 0)

list1 = ["eat", "sleep", "repeat"]
# create enumerate objects 
obj1 = enumerate(list1)
print(list(enumerate(list1)))
# Return = [(0, 'eat'), (1,'sleep'), (2, 'repear')]
 

dranks = ["water", "coffee", "selzer"]
for item in enumerate(dranks):
  print(item)


# Next two loops do the same things 
fruits = ["apple", "banana", "cranberry"]

for i in range(len(fruits)):
  print(i, fruits[i])

for i, j in enumerate(fruits):
  print(i,j)

# Capitalize words w/ even index 
def cap_even(sentence):
  result = [""]
  for i, char in enumerate(sentence):
    result += char.lower() if i % 2 else char.upper()
    
  return result

print(cap_even('joey is not cool'))
