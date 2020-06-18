# Given a number, return mutliplication table up to 50 


def mult_table(num):
  mults = []
  multiple = 1 
  while num* multiple <= 50:
    mults.append(num* multiple) 
    multiple += 1
  return mults

# def mult_table2(n):
#   for i in range(1,11,1):
#     product = n * i 
#     print(product)


print(mult_table(10)) # 10 20 30 40 50 
print(mult_table(15)) # 15 30 45
print(mult_table(7)) # 7 14 21 28 35 42 49


# print(mult_table2(10)) # 10 20 30 40 50 
# print(mult_table2(15)) # 15 30 45
# print(mult_table2(7)) # 7 14 21 28 35 42 49