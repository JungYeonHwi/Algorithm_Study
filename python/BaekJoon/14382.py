def ps(arr, num, i) :
    if sum(list(map(int, arr))) >= 45 and '0' in arr:
        print('Case #' + str(i + 1) + ': ' + str(num))

def sb(arr) :
    return sum(list(map(int, arr))) >= 45 and '0' in arr

t = int(input())

for i in range(t):
    n = int(input())

    if n == 0:
        print('Case #' + str(i + 1) + ': INSOMNIA')
        continue

    numbers = []
    d = 1
    while n <= 10000000 :
        if sb(numbers):
            break

        squares = n
        squares *= d
        for number in str(squares):
            if number not in numbers:
                numbers.append(number)
                ps(numbers, squares, i)

        d += 1