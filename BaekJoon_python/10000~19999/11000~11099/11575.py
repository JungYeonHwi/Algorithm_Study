T = int(input())

for _ in range(T) : 
    a, b = map(int, input().split())
    
    s = input()
    answer = ''.join([chr(ord('A') + ((ord(c)-ord('A'))*a + b)%26) for c in s])
    print(answer)