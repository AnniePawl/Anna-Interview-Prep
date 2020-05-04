# Given 2 integers and an arithmetic operator, return result 
# Operator options: add, subtract, divide, multiply

def arithmetic(a, b, operator):
  if operator == "add":
    return a + b 
  elif operator == "subtract":
    return a - b
  elif operator == "divide":
    return a/b
  else:
    return a * b

def arithmetic_v2(a, b, operator):
  return {
    'add': a + b, 
    'subtract': a - b, 
    'multiply': a * b, 
    'divide': a /b
  } [operator]

print(arithmetic(10,5, "add")) # 15
print(arithmetic(10,5, "subtract")) # 5
print(arithmetic(10,5, "divide")) # 2
print(arithmetic(10,5, "multiply")) # 50