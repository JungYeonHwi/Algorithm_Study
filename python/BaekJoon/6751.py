n = list(input())
N = int("".join(n))
N += 1

while 1 : 
    n = list(str(N))
    if len(set(n)) == len(n) : 
        print(N)
        break
    else : N += 1