# Given an int greater than 9, print its last two digits in reverse order with space between 


# Method One
def swap_last_two(num):
  num_list = [x for x in str(num)]
  return " ".join(map(str,num_list[-2:][::-1]))

print(swap_last_two(1234)) # 4 3 


# Method Two 
def swap_last_two2(num):
  print( num % 10, num%100 //10, end = " ")
  

print(swap_last_two2(9876)) # 6 7 