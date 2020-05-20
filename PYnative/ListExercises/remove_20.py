# Given list, remove all occurannces of specified value

def remove_value(nums, num):
  return [value for value in nums if value != num]

print(remove_value([10,20,20,10,20], 20)) # [10,10]
print(remove_value([20,20,20], 20)) # []
print(remove_value([50,60,40], 60)) # [50,40]
