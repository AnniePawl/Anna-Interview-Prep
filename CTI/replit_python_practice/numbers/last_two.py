# Return last two nums as int

def last_two(num):
  num_list = [x for x in str(num)]
  return int("".join(map(str, num_list[-2:])))

 

print(last_two(123456)) # 56