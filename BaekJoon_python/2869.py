A, B, V = map(int,input().split())

high = V - A

if high % (A-B) == 0 : result = int(high/(A-B))
else : result = int(high/(A-B) + 1)
print(result + 1)