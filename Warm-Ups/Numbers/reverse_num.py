# Given an int, reverse num with space between 

def reverse_num(num):
  reversed_num_list = [x for x in str(num)][::-1]
  return " ".join(reversed_num_list)

print(reverse_num(1234)) # 4 3 2 1

