
n, m = map(int, input().split())
cont = 1
if (1 < n < 20) and (n < m < 100000):

    for i in range(1,((m//n)+1)):
        r = ""
        for j in range(n):
            r += str(cont) + " "
            cont += 1
        print(r[:-1])