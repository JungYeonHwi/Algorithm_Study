N = int(input())
arr = [input() for _ in range(N)]
answer = sum([int(s[:-1])**int(s[-1]) for s in arr])

print(answer)