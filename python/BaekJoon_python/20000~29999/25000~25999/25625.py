x, y = map(int, input().split())

value = y // x % 2

if value == 0 : print(y % x + x)
else : print(y % x)