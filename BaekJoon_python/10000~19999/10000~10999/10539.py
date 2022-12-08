n = int(input())
s = list(map(int, input().split()))

List = []
List.append(s[0])

for i in range(1, n) :
    List.append((s[i] * (i + 1)) - sum(List))
for i in List :
    print(i, end=' ')