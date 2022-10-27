n = int(input())
s = input()
v = 0

for i in s : 
    if i in ['a', 'e', 'i', 'o', 'u'] : v += 1

print(v)