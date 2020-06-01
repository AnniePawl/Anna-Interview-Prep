# Write a function that takes in two lists (a and b), annd returns a list of common values in both sets 

# Clarifying Qs: are inputs same type?

# Brue Force 
# Time Complexity : O(n) b/c for loop
def common_vals_brute_force(a, b):
  common_values = []
  for item in b:
    if item in a:
      common_values.append(item)
  return common_values

# Brute Force 2, List Comprehension 
# Time Complexity : O(n) b/c for loop
def common_vals_brute_force2(a, b):
  return [item for item in b if item in a]


# Set Strategy 
def common_vals_set(a, b):
  return set(a).intersection(set(b))


# TEST
a = [1,"button",2,3,"toot", 4, True, 5]
b = [4, False,5,"cookie", 6,7, "toot", 8]
print(common_vals_brute_force(a, b)) # [4,5,'toot']
print(common_vals_brute_force2(a, b)) # [4,5, 'toot']
print(common_vals_set(a, b)) # [4,5, 'toot']