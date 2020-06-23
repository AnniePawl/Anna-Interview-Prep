# Given 2 python lists, iterate over both simultaneously such that list 1 displays item in original order and list2 in reverse order 



list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

# Example Output 
# 10 400
# 20 300
# 30 200
# 40 100