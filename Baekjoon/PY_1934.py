T = int(input())

for i in range(T):
    A, B = map(int, input().split())

    a, b = A, B
    while a != 0:
        b = b % a
        a, b = b, a

    gcd = b
    lcm = A * B // b
    print(lcm)

