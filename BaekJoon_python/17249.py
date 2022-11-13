s = input()

check = "(^0^)"

idx = s.index(check)
left = s[:idx]
right = s[idx+5:]

l = left.count("@")
r = right.count("@")

print(l, r)