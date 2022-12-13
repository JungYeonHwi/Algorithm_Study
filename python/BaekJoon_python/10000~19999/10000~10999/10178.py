N = int(input())

for _ in range(N) : 
    x, y = map(int, input().split())
    print('You get %d piece(s) and your dad gets %d piece(s).'%((x//y), x%y))