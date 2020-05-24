# Given array of its, 1st goes into team 1, second into team 2, etc . Return new array/tuple w/ two ints. First is sum of team 1, second is sum of team 2. 

# Brute force solution 
def row_weights(array):
  teamA = []
  teamB = []
  for i in range(len(array)):
    if i % 2 == 0:
      teamA.append(array[i])
    else:
      teamB.append(array[i])
  return (sum(teamA), sum(teamB))
  
def row_weights2(array):
  return (sum(array[i] for i in range(len(array)) if i % 2 ==0), sum(array[i] for i in range(len(array)) if i % 2 !=0))


def row_weights3(array):
  return sum(array[::2]), sum(array[1::2])


print(row_weights([80])) # (80,0)
print(row_weights([100,150])) # (100.,150)
print(row_weights([50,60,70,80])) # (120,140) -> 50+70, 60+80

print(row_weights2([80])) # (80,0)
print(row_weights2([100,150])) # (100,150)
print(row_weights2([50,60,70,80])) # (120,140) -> 50+70, 60+80

print(row_weights3([80])) # (80,0)
print(row_weights3([100,150])) # (100,150)
print(row_weights3([50,60,70,80])) # (120,140) -> 50+70, 60+80