for _ in range(int(input())):
    w, n = map(int, input().split())
    testcase = []
    for __ in range(n):
        xi, wi = map(int, input().split())
        testcase.append([xi, wi])

    capacity = 0
    distance = 0
    pv = 0
    for i in testcase:
        if capacity + i[1] < w:
            distance += i[0] - pv
            capacity += i[1]
        elif capacity + i[1] == w:
            distance += (i[0] - pv) + i[0] * 2
            capacity = 0
            if testcase.index(i) == n - 1:
                distance -= i[0] * 2
        elif capacity + i[1] > w:
            capacity = i[1]
            distance += (i[0] - pv) + i[0] * 2
        pv = i[0]

    if testcase.index(i) == n - 1:
        distance += i[0]

    print(distance)