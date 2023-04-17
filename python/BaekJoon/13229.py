n = int(input())
arr = list(map(int, input().split()))
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(sum(arr[a:b+1]))