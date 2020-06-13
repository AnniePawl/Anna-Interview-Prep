# Without using build in square root functions, return in of input's square root. Don't round 

def square_root(num):
  return int(num ** .5)

print(square_root(4)) # 2
print(square_root(8)) # 2 b/c 2.8282.. turned to int


# CTI Solution 
def squareRoot(num):
    """
    :type x: int
    :rtype: int
    """
    lower = 0
    upper = num
    
    while upper >= lower:
        mid = (lower + upper) >> 1
        
        current = mid * mid
        
        if current == num:
            return mid
        elif current > num:
            upper = mid - 1
        elif current < num:
            lower = mid + 1
    
    return upper
