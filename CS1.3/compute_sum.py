# Computer Sum() takes in n, returns 10 if n = 4


def compute_sum_iterative(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum


def compute_sum_recursive(n):
    if n == 1:  # base case
        return n
    else:
        return n + compute_sum_recursive(n-1)


print(compute_sum_iterative(4))
print(compute_sum_recursive(5))
