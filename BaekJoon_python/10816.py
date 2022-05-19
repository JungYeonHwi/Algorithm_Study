from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
check = list(map(int,stdin.readline().split()))

count = Counter(card)

for i in range(len(check)) :
    if check[i] in count : print(count[check[i]], end=' ')
    else : print(0, end=' ')