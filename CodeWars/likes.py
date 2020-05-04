# Implement function that takes in array containing names and returns properly formatted sentence 

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)



print(likes([])) # "No one likes this"
print(likes(['Anna', 'Joey'])) # "Joey and Anna like this"
print(likes(['Anna', 'Joey', 'Kat'])) # "Anna, Joey and Kat like this"
print(likes(['Anna', 'Joey', 'Kat', 'Boo', 'Winnie', 'Bella'])) # "Anna, Joey, Kat, and 3 others like this 