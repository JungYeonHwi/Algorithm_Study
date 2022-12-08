n = int(input())
s = input()

count = s.count('LL')
if (count <= 1) : print(len(s))
else : print(len(s) - count + 1)