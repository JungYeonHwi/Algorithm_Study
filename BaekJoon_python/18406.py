List = list(map(int, input()))
a = sum(List[:len(List) // 2])
b = sum(List[len(List) // 2:])

if a == b : print('LUCKY')
else : print('READY')