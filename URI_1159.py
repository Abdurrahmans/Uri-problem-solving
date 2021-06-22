while True:
    n = int(input())
    sum = 0
    if n == 0:
        break
    else:
        if n % 2 == 0:
            for j in range(1, 6):
                sum += n
                n += 2
            print(sum)
        else:
            sum = 0
            n = n + 1
            for j in range(1, 6):
                sum += n
                n = n + 2
            print(sum)
