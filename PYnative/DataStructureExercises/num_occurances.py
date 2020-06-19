# Given a list of nums, return dictionary with count of occurances of each 

def num_occurances(nums):
  count_dict = {}
  for num in nums:
    if num in count_dict:
      count_dict[num] +=1
    else: 
      count_dict[num] = 1
  return count_dict

print(num_occurances([1,2,2,3,3,3,4,4,4,4])) #{1:1, 2:2, 3:3, 4:4}