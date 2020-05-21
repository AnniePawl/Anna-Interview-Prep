# Return array where first elemnts if the count of how many positive ints there are, and second is sum of negative nnumbers 

def count_sum(nums):
  pos_count = 0
  neg_sum = 0

  for num in nums:
    if num > 0:
      pos_count +=1 
    else:
      neg_sum += num
  return [pos_count, neg_sum]

def count_sum2(nums):
  pos_count = sum(1 for num in nums if num >0)
  neg_sum = sum(num for num in nums if num <0 )
  return [pos_count, neg_sum]

def count_sum3(nums):
  return [sum(1 for num in nums if num >0), sum(num for num in nums if num<0)] if nums else []


print(count_sum([1,2,3,-1,-2,-3])) # [3, -6]
print(count_sum2([1,2,3,-1,-2,-3])) # [3, -6]
print(count_sum3([1,2,3,-1,-2,-3])) # [3, -6]
print(count_sum3([0,0])) # [0,0]
print(count_sum3([])) # []