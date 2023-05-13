S = list(str(input()))
high = 0
for i in range(len(S)):
    if i == 0:
        high += 10
    elif S[i] == S[i - 1]:
        high += 5
    else:
        high += 10

print(high)
