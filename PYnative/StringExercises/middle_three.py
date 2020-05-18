# Given string of off length, return new string made of 3 middle characters 

def middle_three(str):
  middle_index = len(str)//2
  return str[middle_index-1:middle_index+2]


print(middle_three('Goopy')) # oop
print(middle_three('america')) # eri