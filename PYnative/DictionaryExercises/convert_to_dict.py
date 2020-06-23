# Given list of keys and list of values, convert into dictionary 

def convert(keys, values):
  my_dict = dict(zip(keys,values))
  return my_dict

print(convert(['Ten', 'Twenty', 'Thirty'],[10, 20, 30] ))
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}