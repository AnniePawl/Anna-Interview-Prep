# Find sum of odd numbers in array after cubing initial ints. Return None or NULL if any item is not a number 

def sum_cube_odd(arr):
  cubes = []
  for item in arr:
    if str(item).strip('-').isnumeric() == False:
      return "None"
    else:
      if item % 2 != 0:
        cubes.append(item**3)
  return sum(cubes)

print(sum_cube_odd([1,2,3,4])) # 28
print(sum_cube_odd([-3,-2,2,3])) # 0
print(sum_cube_odd([-3,-2,'a',3])) # None
