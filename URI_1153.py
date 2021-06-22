
n = int(input())
if 0 < n < 13:
    f = 1
    for x in range(1, n+1):
        f = f * x
    print(f)