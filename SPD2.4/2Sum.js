// PROBLEM
// Given an array a of n numbers and a target value t, find two numbers whose sum is t.

// EXAMPLES
// a=[5, 3, 6, 8, 2, 4, 7], t=10  ⇒  [3, 7] or [6, 4] or [8, 2]
// a=[2,3,4,5,6,7,8], t =10

//SOLUTION ONE
// Time Complexity: O(n)^2
function target(a, t) {
  for (let i = 0; i < a.length - 1; i++) {
    //o(n)
    for (let j = i + 1; j < a.length; j++) {
      //o(n)
      // check if i and j = target
      if (a[i] + a[j] === t) {
        return [a[i], a[j]];
      }
    }
  }
}

console.log(target([5, 3, 6, 8, 2, 4, 7], 8));

// SOLUTION TWO
// Time Complexity: 0(n log n)
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

console.log(target2([5, 3, 6, 8, 2, 4, 7], 10));

// SOLUTION ONE PSEUDOCODE
// Start at first number in array (index 0) - this is focal number
// Check if focal number + following number (i+1) = target
// If not, check if focal number + next num = target until out of numbers to check
// If target not found in that round, move focal number to index 1
// Return to step 2
// When numbers add to target, return those numbers

// SOLUTION TWO PSEUDOCODE
// take orginal array and sort // nlogn
// assign variable to leftmost and rightmost values (low, high)
// create while loop to track 2 varaiables o(n)
// if variables = t , return those variables
// if variables > t, decrement high var
// if variable <t, increment low var

// More time efficient solution (but less space efficient)
// Create a dictionary and store difference (sum-current) ?
