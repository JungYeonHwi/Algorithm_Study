A, B, C = map(int, input().split())

answer = max([A, B, C]) * 3 - sum([A, B, C])
print(answer)