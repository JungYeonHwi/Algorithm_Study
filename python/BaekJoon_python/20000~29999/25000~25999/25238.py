a, b = map(int, input().split())

qkdan = a * b / 100
qkddjdbf = a - qkdan

if qkddjdbf < 100 : print(1)
else : print(0)