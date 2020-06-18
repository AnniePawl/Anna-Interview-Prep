# Return total number of digits in given number


def digits(num):
 num_list = [num for num in str(num)]
 return len(num_list)

print(digits(98746)) # 5 
print(digits(9874694850)) # 10



num = 75869
count = 0
while num != 0:
    num //= 10
    count+= 1
print("Total digits are: ", count)