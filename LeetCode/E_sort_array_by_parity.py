# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition

# Example input and output:
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Lambda?


class Solution(object):
    def sortArrayByParity(self, A):
        evens = []
        odds = []

        for n in number:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
            return evens+odds

        """
            :type A: List[int]
            :rtype: List[int]
            """
