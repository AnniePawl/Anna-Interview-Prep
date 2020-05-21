# Return new array consisting of elements which are multiple of their own index

def mult_of_index(nums):
  mults_array = []
  for i in range(1,len(nums)):
    if nums[i] % i == 0:
      mults_array.append(nums[i])
  return mults_array

def mult_of_index2(nums):
  return [nums[i] for i in range(1,len(nums)) if nums[i]% i ==0]

  

print(mult_of_index([22,-6,32,82,9,25])) # [-6,32,25]
print(mult_of_index2([22,-6,32,82,9,25])) # [-6,32,25]