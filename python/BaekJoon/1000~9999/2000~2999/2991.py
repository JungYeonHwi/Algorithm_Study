A, B, C, D = map(int, input().split())
arr = list(map(int, input().split()))

for n in arr :
    attacked = 0
    if 0 < n % (A+B) <= A : attacked += 1
    if 0 < n % (C+D) <= C : attacked += 1
    print(attacked)