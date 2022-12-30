n = int(input())
s1, s2 = input(), input()
cnt = 0
for i in range(n) :
    if s1[i] == s2[i] :
        cnt += 1
print(cnt)