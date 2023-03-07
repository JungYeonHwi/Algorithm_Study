w = int(input())
l = int(input())
h = int(input())

r = min(w, l)
w = max(w, l)

if max(r, h) / min(r, h) >= 2 and w / r < 2 : print("good")
else : print("bad")