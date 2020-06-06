# Return the nth Fibonnacci number 

def fibonnacci(n):
  # base cases
  if n == 0:
    return 0 
  if n == 1:
    return 1 
  if n > 1:
    return fibonnacci(n-1) + fibonnacci(n-2)


print(fibonnacci(6))

# CTI Soltition 
prev, next = 1, 1
n = int(input())
for i in range(n-2):
  prev, next = next, prev + next
print(next )