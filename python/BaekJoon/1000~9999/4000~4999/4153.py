while 1 :
    List = list(map(int, input().split()))
    maxNum = max(List)
    if sum(List) == 0 : break
    List.remove(maxNum)
    if List[0] ** 2 + List[1] ** 2 == maxNum ** 2 : print('right')
    else : print('wrong')