# Given two lists, count how many numbers from first occur in second

def intersection_count(s,t):
  return len(set(s).intersection(set(t)))

print(intersection_count([1,2,3], [4,3,2])) # 2 


s = [x for x in input().split(' ')]
t = [x for x in input().split(' ')]
print(s,t)

# CTI Solution 
print(len(set(input().split()) & set(input().split())))