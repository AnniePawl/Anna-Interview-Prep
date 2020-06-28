# Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, followed by one integer c. Multiply every element by c and print the result.


a = [[int(j) for j in input().split()] for i in range(NUM_ROWS)]
c = int(input())


# Sample input 
# 3 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 2

# Sample output 
# 22 24 26 28
# 42 44 46 48
# 62 64 66 68
