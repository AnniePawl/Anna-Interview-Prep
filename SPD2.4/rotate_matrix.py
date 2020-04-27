# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# m =
# [[0, 1, 2, 4],
#  [5, 6, 7, 8],
#  [9, 10, 11, 12],
#  [13, 14, 15, 16]]

#  Example output
# m = [
#     [13, 9, 5, 0],
#     [14, 10, 6, 1],
#     [15, 11, 7, 2],
#     [16, 12, 8, 4]
# ]


# Rotate NxN matrix
def rotate_matrix(m):
    length = len(m)  # Calc length of matrix
    newArray = [[] for _ in range(length)]  # New array w/ N empty arrays
    # loop over rows in  m using index (i)
    for i in range(length-1, -1, -1):  # range(start,end, skip)
        # loop over columns and row using index (j)
        for j in range(length):
            arr = newArray[j]
            item = m[i][j]
            arr.append(item)
            print(f"moved {item} from row {i} to row {j})")
    return newArray


test_case = [
    [0, 1, 2, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(rotate_matrix(test_case))
