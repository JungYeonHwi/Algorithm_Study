n = int(input())

for i in range(n) : 
    name = input()
    
    g = name.count('g') + name.count('G')
    b = name.count('b') + name.count('B')
    
    if g > b : print(f'{name} is GOOD')   
    elif g < b : print(f'{name} is A BADDY')
    else : print(f'{name} is NEUTRAL')