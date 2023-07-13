N = int(input())
S = str(input())
C = list(S)
cnt = []
count = 1
for i in range(1, N):
    if ord(C[i-1]) - ord(C[i]) == 1 or ord(C[i]) - ord(C[i-1]) == 1:
        count = count + 1
    else:
        cnt.append(count)
        count = 1
cnt.append(count)
if max(cnt) >= 5:
    print("YES")
else:
    print("NO")