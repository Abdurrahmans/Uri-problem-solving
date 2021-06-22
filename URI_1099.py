n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    num = 0
    if a == b:
        print(0)
    else:
        c = 0
        if a > b:
            c = a
            a = b
            b = c
        while a < (b-1):
            a += 1
            if a % 2 != 0:
                num += a
        print(num)