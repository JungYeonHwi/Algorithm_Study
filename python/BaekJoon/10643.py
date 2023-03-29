s = []
max = 0
for i in range(8):
    s.append(int(input()))
for i in range(8):
    a = 0
    for j in range(4):
        a += s[j]
    if a > max:
        max = a
    s.append(s[0])
    del s[0]
print(max)