# Given list of whole nums and a target, find two nums whose sum is equal to target  

# Are we optimizing for space or time ?
# Will there always be a solution ? - print any one
# Will there be multiple valid answers ? "no solution"

def sum(nums, target):
  value_dict = {}
  for value in nums:
    if value in value_dict:
      value_dict[value] +=1
    else:
      value_dict[value] = 1  

  print(value_dict)

print(sum([10,20,30,40,50], 30)) # [10,20]
print(sum([10,20,30,40,50], 150)) # "no solution"
print(sum([1,4,3,2], 5)) # "no solution" [1,4], [3,2]