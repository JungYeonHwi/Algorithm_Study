def find(num) : 
    for i in range(1, n+1) :
        if cost[i] <= num : return i
        
def maxIdx() : 
    answer = 0
    maxVote = 0
    for i in range(1, n+1) : 
        if vote[i] > maxVote : 
            maxVote = vote[i]
            answer = i
    
    return answer

n, m = map(int, input().split())
cost = [0] + [int(input()) for _ in range(n)]
vote = [0] * (n + 1)

for _ in range(m) : 
    idx = find(int(input()))
    vote[idx] += 1
    
print(maxIdx())