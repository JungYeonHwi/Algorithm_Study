for _ in range(int(input())):
    num1, num2 = map(int, input().split())
    
    reversedNum1 = int(str(num1)[::-1])
    reversedNum2 = int(str(num2)[::-1])
    
    value = reversedNum1 + reversedNum2
    
    print(int(str(value)[::-1]))