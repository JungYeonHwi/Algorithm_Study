k = int(input())
t = 2**k - 1
answer = t*(t+1)//2
print(bin(answer)[2:])