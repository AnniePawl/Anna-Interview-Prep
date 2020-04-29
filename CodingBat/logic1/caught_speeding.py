# 0 = no ticket, 1= small ticket, 2 = big ticket. If speed is 60 or less, result 0. If speed 61-80, small ticket. If speed over 81, big ticket. Unless it's your birthday- then speed can be 5 higher in all cases. 

def caught_speeding(speed, is_birthday):

    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0

    return 1 if 61 <= speed <= 80 else 2

print(caught_speeding(60, False)) # 0 
print(caught_speeding(65, False)) # 1 
print(caught_speeding(65, True)) # 0
