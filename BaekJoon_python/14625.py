H, M = map(int, input().split())
EH, EM = map(int, input().split())

n = int(input())
c = 0

while 1 : 
    if H % 10 == n or H // 10 == n or M % 10 == n or M // 10 == n : c += 1
    if H == EH and M == EM : break
    M += 1
    if M == 60 : 
        M = 0
        H += 1
    
print(c)