# Given month (1-12) and day(1-31) in 2017
# Return month and day of next day. 

# 30 days 4, 6, 9, 11


month = int(input())
day = int(input())

if ((day == 30) and (month == 4 or month == 6 or month == 9 or month == 11)
    or (day == 28) and (month == 2)
    or (day == 31)):
  month += 1
  day = 1
else:
  day += 1
if month == 13:
  month = 1

print(month)
print(day)

# ////////////////////////////////////////
def next_day(a,b):
  if a in [4,6,9,11]:
    if b == 30:
      print(a + 1)
      print(1)
    else:
      print(a)
      print(b + 1)
  elif a == 2:
    if b == 28:
      print(a + 1)
      print(1)
    else:
      print(a)
      print(b + 1)
  elif a == 12:
    if b == 31:
      print(1)
      print(1)
    else:
      print(a)
      print(b+1)
  else:
    if b == 31:
      print( a + 1)
      print(1)
    else:
      print(a)
      print(b+1)


print(next_day(3,30)) # 3,31
print(next_day(3,31)) # 4,1
print(next_day(2,28)) # 3,1