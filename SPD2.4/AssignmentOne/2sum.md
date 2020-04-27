# PROBLEM ONE PSEUDOCODE

Given an array (a) and of n numbers and a target value(t), find two numbers whose sum is target <br>
Example: <br>
a = [5,3,6,8,2,4,7], t = 10, solution = [3,7] or [6,4], or [8,2]

Brute Force
# function two sum (list, target)
# for each item in list
# for each other item in list
# if item + other item is equal to target
# return those values
Dictionary
# function two sum (list, target)
# init dictionary
# for each item in list
# get complement (target - item)
# if complement is in hashtable
# return those values
# insert its value and index into dictionary

# PROBLEM TWO PSEUDOCODE

Given an array (a) of numbers and a count (k), find the k largest values in the array

Example: a = [5,1,3,6,8,2,4,7], k = 3 => [6,8,7]

# PROBLEM THREE PSEUDOCODE

Given two arrays (a and b) of numbers and a target value(t), find a number from each array whose sum is closest to target(t). <br>
Example <br>
a = [9,13,1,8,2,4,0,5], b = [3,17,4,14,6], t = 20, solution = [13,6] or [4,17] or [5,14]


// SOLUTION 1
// Brute Force
// create a variable closest pair which starts as an array containing the first value of <a> and <b> called <closestPair>
// loop through a with <val1> // O(n)
    // loop through b with <val2> // O(n)
        // if <val1> + <val2> is closer to <t> then the sum of <closestPair>
            // set <closestPair> to [<val1>, <val2>]
// return <closestPair>
// Time Complexity O(n^2) because we loop through the array twice nested
// Space Complexity O(1) because we only create an array with a fixed length of 2


// SOLUTION 2
// slightly more elegant
// sort both <a> and <b> //O(n*log(n))
// create a variable closest pair which starts as an array containing the first value of <a> and the last value of <b> called <closestPair>
// create a variable to store current index for <a> called <aIndex>
// create a variable to store current index for <b> called <bIndex>
// while <aIndex> is less than <bIndex> // worst case O(n)
    // if the sum of <closestPair> is greater than <t>
        // subtract one from <bIndex>
    // else if the sum of <closestPair is less than <t>
        // add one to <aIndex>
    // else // the sum is exactly the same as <t>
        // return <closestPair>
    // if the sum of <a>[<aIndex>] and <b>[<bIndex>] is closer to or equadistant from <t> then sum of <closestPair>
        // set <closestPair> to [<a>[<aIndex>], <b>[<bIndex>]]
    // else
        // return <closestPair>
// Time Complexity O(n*log(n)) because sorting
// Space Complexity O(1) because we only create an array with a fixed length of 2
