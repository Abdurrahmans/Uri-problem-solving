
Alcool = Gasolina = Diesel = 0

while True:
    x = int(input())
    if x==4:
        break
    else:
        if x==1:
            Alcool+=1
        elif x==2:
            Gasolina+=1
        elif x==3:
            Diesel+=1

print('MUITO OBRIGADO')
print('Alcool: {}'.format(Alcool))
print('Gasolina: {}'.format(Gasolina))
print('Diesel: {}'.format(Diesel))