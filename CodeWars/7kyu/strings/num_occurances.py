#  Returnn num of occorances of element in array 

def num_occurances(element, sample):
  return sum(1 for num in sample if num == element)

def num_occurances2(element,sample):
  return sample.count(element)


sample = [1,2,2,3,3,3,4,4,4,4]
print(num_occurances(0,sample)) # 0
print(num_occurances(1,sample)) # 1
print(num_occurances(2,sample)) # 2

print(num_occurances2(0,sample)) # 0
print(num_occurances2(1,sample)) # 1
print(num_occurances2(2,sample)) # 2