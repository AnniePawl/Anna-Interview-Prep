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

