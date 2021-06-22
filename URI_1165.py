n = int(input())
if 1 <= n <= 100:
    for i in range(n):
        x = int(input())
        isPrime = 0
        for j in range(2, x):
            if x % j == 0:
                isPrime = 1
                break
        if isPrime == 0:
            print('{} eh primo'.format(x))
        else:
            print('{}  nao eh primo'.format(x))






