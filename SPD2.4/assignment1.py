# Given an array (a) of n numbers and a count k. Find K largest values in aray a


# SOLUTION ONE (sorting = n log n )


# SOLUTION TWO
def largest_numbers(array, k):
    pass


# Simpler Solution
# Image we are looking for largest numbers in Unosorted array
def simple_largest_num(array):  # overall time o(n)
    largest_num = array[0]  # space o(1)
    for i in range(len(array)):  # time o(n)
        if array[i] > largest_num:  # time 0(1)
            largest_num = array[i]  # time o(1)
    return largest_num


array = [5, 3, 6, 8, 4, 7, 11, 1]
k = 2
# print(simple_largest_num([2, 4, 3, 6]))


# Function that kinds k largest numbers
# k = count, n = length of array
def k_largest_num(array, k):  # time o(k*n)
    result = []  # space o(k)
    while len(result) < k:  # time o(k)
        largest = simple_largest_num(array)  # time o(n)
        array.remove(largest)  # time o(n)
        result.append(largest)  # time o(1)
    return result


print(k_largest_num(array, k))
