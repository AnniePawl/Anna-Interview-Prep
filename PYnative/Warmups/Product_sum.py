# Given 2 integers, return their product. If product greater than 1000, return their sum 

def product_sum(num1, num2):
  return num1 * num2 if num1* num2 < 1000 else num1 +num2
  
print(product_sum(10,55)) # 550  (multiply)
print(product_sum(25,25)) # 625 (multiply)
print(product_sum(86,40)) # 126 (add b/c product > 1000)