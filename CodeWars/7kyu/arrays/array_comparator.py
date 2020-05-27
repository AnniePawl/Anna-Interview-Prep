# Given 2 arrays with unique elements, return number of elements that are in both 


def array_comparator(a,b):
  set1 = set(a)
  set2 = set(b)
  return len(set1.intersection(set2))

def array_comparator2(a,b):
  return len(set(a).intersection(set(b)))

def array_comparator3(a,b):
  return sum(x in b for x in a)

def array_comparator4(a,b):
  return sum(1 for x in a if x in b)

print(array_comparator(['button', 5, True, 'gossip'], [False, 'gossip', 10, 'jumbo', 5])) # 2 (5 and 'gossip)
print(array_comparator2(['button', 5, True, 'gossip', False], [False, 'gossip', 10, 'jumbo', 5])) # 3 (5 and 'gossip, False)
print(array_comparator3(['button', 5, True, 'gossip', False], [False, 'gossip', 10, 'jumbo', 5])) # 3 (5 and 'gossip, False)