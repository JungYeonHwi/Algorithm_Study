cards = {'P':13, 'K':13, 'H':13, 'T':13}
S = input()
s = set()

isSame = False
for idx in range(0, len(S), 3):
    if S[idx:idx+3] in s :
        isSame = True
        print('GRESKA')
        break
    s.add(S[idx:idx+3])
    cards[S[idx]] -= 1

if not isSame :
    print(*cards.values())