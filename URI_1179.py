par = []
impar = []
for i in range(15):
    value = int(input())
    if value % 2 == 0:
        par.append(value)
    else:
        impar.append(value)
    if len(par) == 5:
        j = 0
        for x in par:
            print('par[{0}] = {1}'.format(j, x))
            j = j + 1
        par = []
    if len(impar) == 5:
        j = 0
        for x in impar:
            print('impar[{0}] = {1}'.format(j, x))
            j = j + 1
        impar = []
if len(impar) > 5:
    j = 0
    for x in impar:
        print('impar[{0}] = {1}'.format(j, x))
        j = j + 1

if len(par) > 5:
    j = 0
    for x in arr:
        print('par[{0}] = {1}'.format(j, x))
        j = j + 1

