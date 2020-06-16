# Given a year, determine if it's a leap year. If so, print "LEAP", else print, "COMMON"
# Year is a leap year if its number is exactly divisible by 400 

def leap_year(year):
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('LEAP')
  else:
    print('COMMON')

print(leap_year(2012)) # LEAP
print(leap_year(2021)) # COMMON