a, b = map(int, input().split())

max_value = max(a, b)
min_value = min(a, b)

s = (a + b) * (max_value - min_value +1) / 2

print(int(s))