# Given a year, find respective number of the century. Year can be less than 4 digitsNote that 20th century started in 1901


def century(year):
  return (year - 1) // 100 + 1


# Shitty way
def century2(year):
  year_list = [int(x) for x in str(year)]
  if len(year_list) == 3:
    return year_list[0]
  if year_list[-1] > 0 or year_list[-2] > 0:
    return int("".join(map(str, year_list[:2]))) + 1
  else:
    return ("".join(map(str,year_list[:2])))




print(century(2000)) # 20 
print(century(1901)) # 20 
print(century(1900)) # 19
print(century(785)) # 8