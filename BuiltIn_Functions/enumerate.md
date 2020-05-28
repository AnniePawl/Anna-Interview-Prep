## Enumerate 
Enumerate adds a counter to an iterable and returns it in for of "enumerate object", which can be used directly in for loops or converted into list of tuples using list() method <br>
Allows you to easily iterate over elements AND their index 


### Syntax 
**`enumerate(iterable, start = 0)`**


### Examples 
```python 
animals = ["dog", "horse", "pig"]
object1 = enumerate(animal)
print(list(enumerate(animals)))
```
Using enumerate object in **Loops**
```python 
dranks = ['coffee', 'selzer', 'water']
for item in enumerate(dranks):
  print(item)
```

The following 2 examples accomplish the same things: 
```python 
fruits = ["apple", "banana", "cranberry"]

for i in range(len(fruits)):
  print(i, fruits[i])

for i, j in enumerate(fruits):
  print(i,j)
```

**Capitalize letters w/ even index**
```python 
def alternate_caps2(string):
  s = "".join(c if i%2 else c.upper() for i, c in enumerate(string))
  return [s,s.swapcase()]
```