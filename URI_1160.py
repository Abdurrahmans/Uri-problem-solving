
n = int(input())

for i in range(n):
    a, b, c, d = input().split()
    a = int(a)
    b = int(b)
    c = float(c)
    d = float(d)
    anos = 0
    while a <= b:
        cpa = int(a * (c / 100))
        cpb = int(b * (d / 100))
        anos += 1
        a += cpa
        b += cpb

        if anos > 100:
            break

    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print("{} anos.".format(anos))