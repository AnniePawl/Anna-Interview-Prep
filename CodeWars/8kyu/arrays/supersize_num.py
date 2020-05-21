# Rearrange integer into largest possible value 

def supersize(num):
  num_array = [(i) for i in str(num)]
  num_array.sort(reverse=True)
  # Remember .join only works on strings
  new_num=  "".join(num_array)
  return int(new_num)

def supersize2(num):
  return int("".join(sorted(str(num), reverse=True)))

print(supersize(123456)) #654321
print(supersize(105)) #510

print(supersize2(123456)) #654321
print(supersize2(105)) #510