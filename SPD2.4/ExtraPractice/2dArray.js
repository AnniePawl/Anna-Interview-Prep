//  Given an array of values you need to map the values on to a grid. Return an array of objects containing the original value, and a row and col that would represent the position of where the object would map on the grid. Assume the length of the original array is always a square e.g. 4, 9, 16 etc. Assume the grid has an equal height and width.

// # Sample input
array = [1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 3, 0, 1, 1, 1, 0];

function grid(array) {
  const gridWidth = Math.sqrt(array.length);
  output = [];

  for (let i = 0; i < array.length; i += gridWidth) {
    subarray = array.slice(i, i + gridWidth);
    output.push(subarray);
  }
  return output;
}

console.log(grid(array));
