k, w, m = map(int, input().split())

if (w-k) % m : print((w - k) // m + 1)
else : print((w - k) // m)