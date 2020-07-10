# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# Sort Solution 
# Time Complexity O(n log n)
# Space Complexity O(n)
def sorted_squares(A):
  squares = [num**2 for num in A]
  return sorted(squares)

print(sorted_squares([-4,-1,0,3,10])) # [0,1,9,16,100]
print(sorted_squares([-7,-3,2,3,11])) # [4,9,9,49,121]


# Two Pointer Solution 
# Time Complexity 0(n)
# Space Complexity O(n)
def sortedSquares(self, A):
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ansa