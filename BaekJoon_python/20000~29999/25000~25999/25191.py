n = int(input())
a, b = map(int, input().rstrip().split())

print(min(n, a // 2 + b))