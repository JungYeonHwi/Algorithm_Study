def convert(ti) : 
    tmp = ti
    if ti < 0 : tmp = ti + 2400
    if ti >= 2400 : tmp = ti - 2400
    if tmp % 100 >= 60 : tmp = 100 * (tmp / 100 + 1) + tmp % 100 -60
    if tmp >= 2400 : tmp -= 2400
    
    return tmp

t = int(input())

print(t, "in Ottawa")
print(convert(t - 300), "in Victoria")
print(convert(t - 200), "in Edmonton")
print(convert(t - 100), "in Winnipeg")
print(t, "in Toronto")
print(convert(t + 100), "in Halifax")
print(convert(t + 130), "in St. John's")