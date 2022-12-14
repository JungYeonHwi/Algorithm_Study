T = int(input())

for i in range(T) : 
    N, S = input().split()
    answer = ""
    
    for k in S : 
        answer += int(N) * k
    print(answer)