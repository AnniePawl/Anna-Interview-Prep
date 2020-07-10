# Given an array, return its majority element 

def majority_element(array):
  count_dict = {}
  majority_num = 0
  array_set = set(array)
  for num in array_set:
    count_dict[num] = array.count(num)
  
  return max(count_dict, key=count_dict.get)
  
  

print(majority_element([3,2,2])) # 3
print(majority_element([1,1,1,2,2,1,1])) # 1