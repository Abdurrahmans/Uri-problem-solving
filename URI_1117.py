sum = 0
qte = 0
while qte < 2:
    n = float(input())
    if 0 <= n <= 10:
        sum += n
        qte += 1
    else:
        print("nota invalida")

print("media = {:.2f}".format(sum/2))