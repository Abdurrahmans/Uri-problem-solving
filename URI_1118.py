x = 0
c = 0
while True:
    n = float(input())
    if 0.0 <= n <= 10:
        x += 1
        c += n
        if x == 2:
            print("media = %.2f" % (c / 2))
            value = int(input("novo calculo (1-sim 2-nao)"))
            if value == 1:
                continue
            elif value == 2:
                break
            else:
                value = int(input("novo calculo (1-sim 2-nao)"))

    else:
        print("nota invalida")
