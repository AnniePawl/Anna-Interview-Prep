# Given integer coordinates of 3 verticesl of parallel rectangle. Find 4th coordinte 

def rectangle(coordinates):
  # p1 = coordinates[:2]
  # p2= coordinates[2:4]
  # p3 = coordinates[4:]
  p4 = []
  for num in coordinates[::2]:
    if coordinates.count(num) ==1:
      p4.append(num)
  for num in coordinates[1::2]:
    if coordinates.count(num) ==1:
      p4.append(num)

  return p4


print(rectangle([1,5,7,5,1,10])) # 7,10
print(rectangle([1,5,7,10,1,10])) # 7, 5


# CTI Solution 
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# x3 = int(input())
# y3 = int(input())

if x1 == x2:
  x4 = x3
elif x1 == x3:
  x4 = x2
else:
  x4 = x1
  
if y1 == y2:
  y4 = y3
elif y1 == y3:
  y4 = y2
else:
  y4 = y1
  