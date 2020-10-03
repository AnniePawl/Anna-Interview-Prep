# Given an interger, return it's last two digits swapped


def swap_last_two(num):
  num_list = [x for x in str(num)]
  return int("".join(num_list[-2:][::-1]))

print(swap_last_two(12345)) # 54


def swap_last_two2(num):
  return str(num % 100)[::-1]

print(swap_last_two2(9876)) # 67