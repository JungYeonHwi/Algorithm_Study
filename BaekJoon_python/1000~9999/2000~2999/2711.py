T = int(input())

for i in range(T) : 
    num, s = input().split()
    num = int(num)
    
    List = list(s)
    answer = "".join(List[:num-1] + List[num:])
    print(answer)