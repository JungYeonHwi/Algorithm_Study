for n in range(int(input())):
    dic=[input()for i in range(int(input()))]
    password=[]
    for _ in range(int(input())):
        current=""
        for i in map(int,input().split()[1:]):
            current += dic[i]
        password += current,
    print("Scenario #%d:"%(n+1))
    for p in password:
        print(p)
    print()