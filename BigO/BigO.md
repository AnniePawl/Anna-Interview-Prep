# Big O Notation 
The language used to describe efficiency of algorithms

## Big O 
- Upper bound on time 
- "Worst case" --> How we typically describe algorithm complexity. Worst and expected case are usually the saem 

## Big Theta 
- Lower bound on time 
- Best case scenario --> We rarly discuss best case b/c it's not very useful

## Big Omega 
- Tight bound on runtime (similar to big O)


# Important Rules
## Drop Non-Dominant Terms 
**Examples** </br>
- O(n^2 + n) becomes O(n^2)
- O(n + log n) becomes O(n)
- O(5*2^n + 1000n^100) becomes O(2^n)


## Multi-part algorithms: Add vs. Multiply