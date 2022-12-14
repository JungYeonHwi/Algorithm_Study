b, c, d = map(int, input().split())

burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

result = 0
minValue = min(b, c, d)
for i in range(minValue) : result += (burger[i] + side[i] + drink[i]) * 0.9

result += sum(burger[minValue::])
result += sum(side[minValue::])
result += sum(drink[minValue::])

print(sum(burger) + sum(side) + sum(drink))
print(int(result))