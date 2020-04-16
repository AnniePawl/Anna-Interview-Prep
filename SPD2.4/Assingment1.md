## Code 2 solutions for each of these 3 problems

### Problem 1: Given an array a of n numbers and a target value t, find two numbers whose sum is t.
**Example: a=[5, 3, 6, 8, 2, 4, 7], t=10 ⇒ [3, 7] or [6, 4] or [8, 2]**<br>
**Solution 1:** Time Complexity: 0(n^2), Space Complexity: ?
```javascript
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
```
**Solution 2:** Time Complexity: 0(n log n), Space Complexity: 
```javascript
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
```

### Problem 2: Given an array a of n numbers and a count k find the k largest values in the array a.
**Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3 ⇒ [6, 8, 7]**<br>
**Solution 1:** Time Complexity: , Space Complexity: 


### Problem 3: Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
**Example: a=[9, 13, 1, 8, 12, 4, 0, 5], b=[3, 17, 4, 14, 6], t=20 ⇒ [13, 6] or [4, 17] or [5, 14]** <br>
**Solution 1**
