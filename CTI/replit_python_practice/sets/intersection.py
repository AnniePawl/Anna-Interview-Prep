# Given 2 lists, find all numbers that occur in both. Print them in ascending order

# Sample input:
# 1 2 3 
# 4 3 2
# Answer --> 2 3

# s = set(input().split())
# t = set(input().split())

def ascending_intersection(a,b):
  intersection = set(a).intersection(set(b))
  print(intersection)

  intersection_list = []

  for item in intersection:
    intersection_list.append(item)
  
  intersection_list.sort(key = int)

  
  print(intersection_list)
    

print(ascending_intersection({1,4,12,5,2}, {12,7,1,9,2}))
print(ascending_intersection({82,54, 91, 100, 70, 33, 88, 14, 52, 48, 56, 20, 63, 16, 22, 23, 30, 8, 84, 75, 45}, {10, 44, 77, 90, 43, 75, 25, 24, 5, 21, 71, 70, 83, 68, 18, 92, 81, 57, 27, 67, 48, 6
}))


# CTI Solution 
first = set([int(s) for s in input().split()])
second = set([int(s) for s in input().split()])
print(*sorted(first & second))
