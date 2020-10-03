# Given an int, return sum of digits in int


def sum_digits(num):
  nums = [int(x) for x in str(num)]
  return sum(nums)

print(sum_digits(123)) # 6
print(sum_digits(1234)) # 10

def sum_digits2(num):
  return sum([int(x)for x in str(num)])
  # return sum(map(int, str(num)))
  # return (a // 100 + a // 10 % 10 + a % 10)



print(sum_digits2(123)) # 6
print(sum_digits2(1234)) # 10
