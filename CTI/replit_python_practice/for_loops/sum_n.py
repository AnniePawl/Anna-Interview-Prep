# N nums given in input, print their sum 
# Fist line contains num of integers 

lines = []
while True:
  line = input()
  if line:
    lines.append(line)
  else:
    break 

lines = [int(x) for x in lines]
print(sum(lines))

