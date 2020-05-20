# Convery a number into reversed array of digits 

def reversed_num_array(num):
  return [int(i) for i in str(num)][::-1]

print(reversed_num_array(12345)) # [5,4,3,2,1]
print(reversed_num_array(736)) # [6,3,7]