def gen(num) : 
    if num == 1 : return 1
    elif num == 2 : return 2
    elif num == 3 : return 4
    else : 
        return gen(num-1) + gen(num-2) + gen(num-3)

t = int(input())

for _ in range(t) : 
    n = int(input())
    
    print(gen(n))