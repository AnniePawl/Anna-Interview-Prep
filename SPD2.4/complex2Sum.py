# Given two arrays (a and b) of numbers and a target value(t), find a number from each array whose sum is closest to target(t).

# Example
# a = [9, 13, 1, 8, 2, 4, 0, 5], b = [3, 17, 4, 14, 6], t = 20
# solution = [13, 6] or [4, 17] or [5, 14]

# PSEUDOCODE Solution One
# Sort arrays a and b





def complex2Sum(a,  b, t):
    sortedA = a.sort()
    sortedB = b.sort()
    


function target2(a, t) {
  const newA = [...a];
  newA.sort((a, b) => a - b); // O(nlog(n))
  let start = 0;
  let end = newA.length - 1;
  while (start <= end) {
    const sum = newA[start] + newA[end];
    if (sum === t) {
      return [newA[start], newA[end]];
    }
    if (sum > t) {
      end -= 1;
    } else if (sum < t) {
      start += 1;
    }
  }
}