n = int(input())

arr = list({0 if ((i % 3 == 0) or (i % 5 == 0)) else i for i in range(1, 15)} - {0})

print(((n - 1) // 8) * 15 + arr[n % 8 - 1])