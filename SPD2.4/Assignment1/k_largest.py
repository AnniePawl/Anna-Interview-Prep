# Given an array numbers and a count(k). Find the k largest values in the array 

# SOLUTION ONE -Using Sorting
# Time Complexity: O(nlogn) b/c sorting + O(n)
# Space Complexity:
arr = [4, 3, 27, 30, 9]
k = 2

def return_k_largest_values(arr, k):
    sorted_array = sorted(arr, reverse=True)
    result = []
    for i in range(k):
        result.append(sorted_array[i])
    return result


print("Testing K Largest V1:")
print(return_k_largest_values(arr, k))


# SOLUTION TWO
# Find Largest Num
def simple_largest_num(array):  # overall time o(n)
    largest_num = array[0]  # space o(1)
    for i in range(len(array)):  # time o(n)
        if array[i] > largest_num:  # time 0(1)
            largest_num = array[i]  # time o(1)
    return largest_num

def k_largest_num(array, k):  # time o(k*n)
    result = []  # space o(k)
    while len(result) < k:  # time o(k)
        largest = simple_largest_num(array)  # time o(n)
        array.remove(largest)  # time o(n)
        result.append(largest)  # time o(1)
    return result

print("Testing K Largest V2:")
print(k_largest_num(arr, k))



