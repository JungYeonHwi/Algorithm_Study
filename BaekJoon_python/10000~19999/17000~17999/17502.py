n = int(input())
s = list(input())
for i in range(n) :
    if s[i].isalpha() :
        s[-1-i] = s[i]
for i in range(n) :
    if s[i]=='?' : s[i]='a'

print(''.join(s))