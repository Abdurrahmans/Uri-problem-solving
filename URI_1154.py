avg = 0
sum = 0
qte = 0
while True:
    a = int(input())
    if a >= 0:
        sum += a
        qte += 1
        avg = float(sum/qte)
    else:
        break
print('{:.2f}'.format(avg))

