M, N, K = map(int, input().split())
answer = []
for _ in range(M) : 
    s = input()
    value = ""
    for i in s : 
        value += i * K
    for j in range(K) : 
        answer.append(value)
    
for i in answer : 
    print(i)