# Return Multiplication table for number thru 10 

def mult_table(number):
  count = 1 
  total = number
  while count < 11:
    print(str(count) + " * " + str(number) + " = " + str(total))
    count +=1
    total+= count * number 


def mult_table2(number):
  return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))

print(mult_table(5))
print(mult_table2(3))

# 1 * 5 = 5 
# 2 * 5 = 10 
# 3 * 5 = 15 
# etc ... until 10 