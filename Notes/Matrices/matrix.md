# 2D Lists (Matrices)
2D lists are also known as matrices. They are lists of lists (nested lists)

## Working with matrices 
We can process a 2D array using nested loops.
- First loop iterates over row number 
- Second loop iterates thru elements inside each row. 
These two examples achieve the same output : <br>
``` python 
1 2 3 
4 5 6 
7 8 9
```
Method One 
```python 
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    print(matrix[i][j], end = ' ')
  print()
``` 
Method Two 
```python 
for row in matrix:
  for element in row:
    print(element, end = ' ')
  print()
```

### Calculate Sum of elements in 2D list 
```python 
sum = 0 
for row in maxtix:
  for element in row:
    sum += element 
print(sum)
```