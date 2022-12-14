List = list(map(int, input().split()))

if List == sorted(List) : print('ascending')
elif List == sorted(List, reverse=True) : print('descending')
else : print('mixed')