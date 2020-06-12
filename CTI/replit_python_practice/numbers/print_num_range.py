# Given num, print all non-zero nums up to/ including num 

def num_range(num):
  for num in range(1, num + 1):
    print(num, end = "\n")

print(num_range(6)) # 1 2 3 4 5 