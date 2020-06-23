# Merge two dictionaries into one 

def merge(a,b):
  dict3 = {**a, **b}
  return dict3

print(merge({'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}))
