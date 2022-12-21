N = int(input())
answer = [1, 2] + [i for i in range(3, 3+N-3)] + [997]
print(N)
print(*answer)