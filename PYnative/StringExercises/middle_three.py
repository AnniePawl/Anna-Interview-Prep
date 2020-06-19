# Given string of off length, return new string made of 3 middle characters 

def middle_three(str):
  middle_index = len(str)//2
  return str[middle_index-1:middle_index+2]


print(middle_three('Goopy')) # oop
print(middle_three('america')) # eri

# Extra Practice
# Remember last index not included
def middle_three2(str):
  return str[(len(str)//2)-1: (len(str)//2+2) ]

print(middle_three2("buttons")) # tto

