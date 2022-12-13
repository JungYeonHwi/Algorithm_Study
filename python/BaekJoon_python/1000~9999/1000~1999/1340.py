Month, D, Y, T = input().split()
D = int(D[:-1])
Y = int(Y)
H, M = map(int, T.split(':'))

monthName = ["January" , "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0) : monthDay[1] += 1
total = sum(monthDay) * 24 * 60

lastMonthIdx = monthName.index(Month)
currentTime = (sum(monthDay[:lastMonthIdx]) + D-1) * 24 * 60 + H * 60 + M
print(currentTime/total * 100)