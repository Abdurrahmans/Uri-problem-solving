while True:
    n = int(input())
    if n == 0:
        break
    value = 1
    arr = []
    num = int(n / 2)
    if n % 2 == 1:
        num = num + 1
    for l in range(1, num):
        for i in range(n):
            for j in range(n):
                arr[i][j] = 1
    for i in range(n):
        for j in range(n):
            print(arr[i][j])
        print(" ")
