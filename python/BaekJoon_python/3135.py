A, B = map(int, input().split())
N = int(input())

record = [abs(int(input())-B) for i in range(N)]

print(min(abs(A-B), min(record)+1))