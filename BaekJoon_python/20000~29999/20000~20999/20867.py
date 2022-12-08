m ,s, g = map(float, input().split())
a, b = map(float, input().split())
l, r = map(float, input().split())

fr = float(1 / a) * float(l) + (m/g)
la = float(1 / b) * float(r) + (m/s)

if (fr < la) : print("friskus")
else : print("latmask")