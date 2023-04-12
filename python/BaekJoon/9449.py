W, H, w, h = map(int, input().split())

result = ((W / w + 1) / 2) * ((H / h + 1) / 2)

print(result)