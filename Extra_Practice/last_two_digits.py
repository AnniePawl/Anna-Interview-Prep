# Given large int, return its last two digits 

# Method One
def last_two_digits(num):
  num_list = [x for x in str(num)]
  return "".join(num_list[-2:])
  
print(last_two_digits(1234)) # 34


# Method Two 
def last_two_digits2(num):
  return "".join(map(str,(num%100//10, num % 10)))

print(last_two_digits2(6789)) # 89