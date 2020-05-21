# Function takes in 2 arguments and returns all numbers which are divisible by given divisor 

def divisible_by(nums, divisor):
  return [num for num in nums if num % divisor == 0]

print(divisible_by([1,2,3,4,5,6,7,8,9,10], 2)) # 2,4,6,8,10
print(divisible_by([1,3,4,9], 3)) # 3,9