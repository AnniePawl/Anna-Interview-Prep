# Given an array of integers, find contiguous sequence w/ largest sum. Return sum

# Input [2, -8, 3, -2, 4, -10]
# Output 5, using [3, -2, 4]


def contiguous_sequence(nums): # Time: O(n), Space: O(1)
    # Track largest sum, initialize to first value
    largest_sum = nums[0]
    # Loop over array using index:
    for i in range(len(nums)):
        # Initialize current sum as value at index
        current_sum = nums[i]
        # Compare curret sum to largest 
        if current_sum > largest_sum:
            #  If it's greater, update largest sum to current 
            largest_sum = current_sum
        # Loop over array from index + 1, j
        for j in range(i + 1, len(nums)):
            # Add value at j to current sum 
            current_sum += nums[j]
            # Compare current sum to largest 
            if current_sum > largest_sum:
                # If it's greater, update largest to current
                largest_sum = current_sum
    return largest_sum


print(contiguous_sequence([2, -8, 3, -2, 4, -10])) # 5
print(contiguous_sequence([2, -8, 5, -2, 4, -10])) # 7


def max_subarray(a, size):
    max_so_far = -1000 # max int
    max_ending_here = 0 # current sum 

    for i in range(0, size):
        # add current num at i to current sum
        max_ending_here = max_ending_here + a[i]
        # If current sum larger, update largest sum
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        
        # If current nsum negative, we dont want to use it to add more nums, so we set it to 0
        if max_ending_here <0:
            max_ending_here = 0 
    return max_so_far

a= [2, -8, 3, -2, 4, -10]
print(max_subarray(a ,len(a)))