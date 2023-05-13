T = int(input())

for i in range(T):
    N = int(input())
    M = 0
    name = ''
    for j in range(N):
        S, L = input().split()
        L = int(L)
        if (L > M):
            M = L
            name = S

    print(name)
