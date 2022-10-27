g, p, t = map(int, input().split())

group = p * t + g
whole = g * p

if group > whole : print(1)
elif group < whole : print(2)
else : print(0)
