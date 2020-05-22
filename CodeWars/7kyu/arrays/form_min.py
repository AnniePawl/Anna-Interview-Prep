# Return smaller number that can be formed from digits using each digit only once. Ignore duplicates 


def form_min(nums):
  num_string = map(str, nums)
  num_set = sorted(set(num_string))
  return "".join(num_set)

def form_min2(nums):
  return int("".join(sorted(set(map(str,nums)))))
  
  

print(form_min([3,1,1])) #13
print(form_min([7,4,5,7])) # 457



print(form_min2([3,1,1])) #13
print(form_min2([7,4,5,7])) # 457