def remove_empty(s):
  for name in s:
    if name == None or name == "":
      s.remove(name)
  return s

def remove_empty2(s):
  # built in function filter
  new_s = list(filter(None, s))
  return new_s


print(remove_empty(['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']))  
print(remove_empty2(['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']))  
# ['Emma', 'Jon', 'Kelly', 'Eric']

