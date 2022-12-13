def change(a, b) :
    tmp = []
    while a > 0 : 
        tmp.append(a % b)
        a = a // b
    tmp = tmp[::-1]
    return tmp

def check(s) : 
    for i in range(len(s)//2) : 
        if s[i] != s[-i-1] : return False

    return True

for _ in range(int(input())) : 
    cnt = False
    n = int(input())
    for i in range(2, 65) : 
        if check(change(n, i)) : 
            cnt = check(change(n, i))
            break
    
    if cnt : print(1)
    else : print(0)