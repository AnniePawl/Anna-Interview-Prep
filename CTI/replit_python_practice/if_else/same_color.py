
# Given 4 ints (two chess coordinates), return YES if they are both the same color, else return NO 


# Better solution 
if (x1 + y1) % 2 == (x2 + y2) % 2:
  print('YES')
else:
  print('NO')




def same_color(a,b,c,d):
  if ((a+b) % 2 == 0 and (c+d) % 2 == 0):
    return "YES"
  elif ((a+b) % 2 != 0 and (c+d) % 2 != 0):
    return "YES"
  else:
    return "NO"
print(same_color(1, 1, 2, 6)) # YES


