import sys
input = sys.stdin.readline

result =[]

n, k = map(int,input().split())
a = list(map(int, input().split()))

for i in range(n - k + 1):
    result.append(sum(a[i:i+k]))
        
print(max(result))