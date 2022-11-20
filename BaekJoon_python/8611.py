from sys import stdin

n = int(stdin.readline())
tmp = True

for b in range(2, 10) : 
    number = n
    m = ''
    
    while number >= b : 
        m += str(number % b)
        number //= b
    
    m += str(number)
        
    if m == m[::-1] : 
        tmp = False
        print(f'{b} {m}')
    
if str(n) == str(n)[::-1] : print(f'10 {n}')
elif tmp : print("NIE")