# Take num as string, return True if divisible by 3 

def divisible_by_3(num):
  num_list = [int(num) for num in num]
  return sum(num_list) % 3 == 0

def divisible_by_3_v2(num):
  return int(num) % 3 == 0


print(divisible_by_3("123")) # True 
print(divisible_by_3("100853")) # False
print(divisible_by_3("333")) # True
