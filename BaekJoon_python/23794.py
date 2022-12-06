N = int(input())

answer = ['' for _ in range(N+2)]
answer[0] = answer[-1] = ( N + 2 ) * "@"

for idx in range(1, N+1):
    answer[idx] = f"@{' '* N}@"
    
print("\n".join(answer))