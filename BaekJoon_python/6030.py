def prime(num) : 
    answer = []
    for i in range(1, num + 1) : 
        if num % i == 0 : 
            answer.append(i)
    return answer

P, Q = map(int, input().split())

p = prime(P)
q = prime(Q)

for i in p : 
    for j in q : 
        print(i, j)