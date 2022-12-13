N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = 1
for n in arr : answer *= n
print(answer % M)