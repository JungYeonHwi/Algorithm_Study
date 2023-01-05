for _ in range(int(input())):
        input()

        answer = sum(map(int, input().split()))

        print('Right' if answer > 0 else ('Left' if answer < 0 else 'Equilibrium'))