# Return 1 if pos, -1 if neg 

# Read an integer:
a = int(input())
# Print a value:
if a == 0:
  print(0)
elif a < 0:
  print(1)
else:
  print(-1)

# Given 2 ints, return "YES" if one is pos and one is neg, else NO
# Read an integer:
a = int(input())
b = int(input())
# Print a value:
if a <0 and b >0 or a> 0 and b <0:
  print("YES")
else:
  print("NO")
