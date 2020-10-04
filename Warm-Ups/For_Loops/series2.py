# Given two ints, A and B, print numbers from A to B inclusively 

def series2(a,b):
  series = []
  for num in range(a,b+1):
    # print(num, end=" ")
    series.append(num)
  return " ".join(map(str,series))

print(series2(5,8)) # 5 6 7 8 
print(series2(9,14)) # 9 10 11 12 13 14