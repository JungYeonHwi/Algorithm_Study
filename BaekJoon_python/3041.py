num = 0
for i in range(4)  :
    s = list(input())
    for j in range(4):
        if s[j] != '.' :
            num += abs((ord(s[j]) - ord('A')) % 4 - j)
            num += abs((ord(s[j]) - ord('A')) // 4 - i)
print(num)