# given numRows, generate numRows of Pascal's triangle 
# To generaate A[C] in row R, sum up A[C] and A[C-1] from previous row R-1
# Since it's an interative problem, use a for loop

# def pascals_triangle(numRows):
  # triangle = []
  # for i in range(1,numRows+1):
  #   for j in range(i+1):
  #     triangle.append(j)
  #     print(triangle, end = "\n")



# print(pascals_triangle(5))
# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]

# rows = 8;
# triangle = [];

# for i in range(rows):
#   row = [];
#   row.append(1);
#   for j in range(i):
#       row.append(2+j);
#   triangle.append(row);
    
# print(triangle)

# Stepping Stones 
n = 5 
print ("1" * n,  end = ' ')
print (str(1) * n, end = ' ')


int_list = [1,3,3,1]
result = [1,4,6,4,1]

for i in range(len(int_list)):
  


# Given a list of ints , print row w/ len(int) + 1
# First and last nume printed will be 1 
# ith num will be sum of value of ith value one 
