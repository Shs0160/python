T = int(input())


for i in range(T):
    a = list(input().split())
    b = float(a[0])
    for j in range(len(a)):

        if a[j] == '#':
            b -= 7
        elif a[j] == '%':
            b += 5
        elif a[j] == '@':
            b += 3

    print('%0.02f' % b)
    