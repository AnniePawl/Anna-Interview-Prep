# Return last two digits in reverse order with space inbetween 

num = 2009 # return 90
num_list = [x for x in str(num)]
print (" ".join((num_list[-2:])[::-1]))

# Reverse num with spaces in between 
num = 1234 # return string 4 3 2 1 
reverse_nums_list = [x for x in str(num)][::-1]

print(" ".join(reverse_nums_list))

# Reverse num, return as number
num = 5678 # return int 8765
reversed_num_list = [x for x in str(num)][::-1]
print(int("".join(reversed_num_list)))