import math

s = int(input())
a = int(input())
b = int(input())

p = 250

if s <= a : print(p)
else : print(p + 100 * math.ceil((s - a) / b))