import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bus = list(map(int, input().split()))
fee = []
for i in range(n) : fee.append(list(map(int, input().split())))
ans = 0
for i in range(m-1):
    ans += fee[bus[i]-1][bus[i+1]-1] 
print(ans)