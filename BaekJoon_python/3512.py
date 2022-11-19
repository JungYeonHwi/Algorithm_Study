n, price = map(int,input().split())
t = 0
bedroom = 0
balcony = 0
for _ in range(n) :
    s, room=input().split()
    if room == 'bedroom' : bedroom = int(s)
    elif room == 'balcony' : balcony = int(s)
    t += int(s)
print(t)
print(bedroom)
print('{:.6f}'.format(price * (t - balcony / 2)))
