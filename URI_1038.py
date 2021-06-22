X,Y = map(int,input().split())
if X == 1:
    price = float(Y*4.00)
elif X == 2:
    price = float(Y*4.50)
elif X == 3:
    price = float(Y*5.00)
elif X == 4:
    price = float(Y*2.00)
elif X == 5:
    price = float(Y*1.50)

print('Total: R$ {:.2f}'.format(price))