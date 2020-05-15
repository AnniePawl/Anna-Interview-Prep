# Given an array of values you need to map the values on to a grid. Return an array of objects containing the original value, and a row and col that would represent the position of where the object would map on the grid. Assume the length of the original array is always a square e.g. 4, 9, 16 etc. Assume the grid has an equal height and width.


# Sample input
array = [1, 2, 1, 1,
         1, 2, 2, 1,
         1, 2, 3, 0,
         1, 1, 1, 0]

# Sample output
# [[1,2,1,1],
# [1,2,2,1],
# [1,2,3,0],
# [1,1,1,0]]


def grid(array):
    length = len(array)  # length = 16 items
    width = int(length ** .5)
    output = []
    for i in range(0, length, width):
        subarray = array[i:i+width]
        output.append(subarray)
    return output


print(grid(array))
