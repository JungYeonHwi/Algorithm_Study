from sys import stdin

for _ in range(3) :
    N = int(stdin.readline())
    List = [int(stdin.readline()) for i in range(N)]
    
    if sum(List) == 0 : print("0")
    elif sum(List) > 0 : print("+")
    else : print("-")