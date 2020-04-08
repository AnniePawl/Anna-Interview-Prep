// Given an array a of n numbers and a target value t, find two numbers whose sum is t.

// a=[5, 3, 6, 8, 2, 4, 7], t=10  ⇒  [3, 7] or [6, 4] or [8, 2]
// a=[2,3,4,5,6,7,8], t =10

// take orginal array and sort // nlogn
// assign variable to leftmost and rightmost values (low, high)
// create while loop to track 2 varaiables o(n)
// if variables = t , return those variables
// if variables > t, decrement high var
// if variable <t, increment low var

// More time efficient solution (but less space efficient)
// Create a dictionary and store difference (sum-current)

function target(a, t) {
  //0(n^2)
  // start at 0
  // add value at index 0 to all other values in array
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

// Simplify Problem
// No duplicates
// Already sorted
// Target is actually in array
// Perfect match
// No negatives
// There are only 2 values and they = 7

// Restate the problem
// Ask clarifying questions
// State your assumptions
// Think out loud
// Brainstorm solutions
// Explain your rationale
// Discuss tradeoffs
// Suggest improvements

// sort number sin array

function target(a, t) {
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
