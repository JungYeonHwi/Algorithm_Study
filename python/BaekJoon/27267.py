a, b, c, d = map(int, input().split())

akti = a * b
vpxmdi = c * d

if akti > vpxmdi : print("M")
elif akti < vpxmdi : print("P")
else : print("E")