
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    sum = 0
    if x % 2 == 1:
        for j in range(1, y+1):
            sum += x
            x = x + 2
        print(sum)
    else:
        sum = 0
        x = x + 1
        for j in range(1, y+1):
            sum += x
            x = x + 2
        print(sum)

