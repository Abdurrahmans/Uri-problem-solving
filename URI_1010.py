code1,units1,price1= input().split(' ')
code2,units2,price2= input().split(' ')
calculate_paid_amount =(int(units1)*float(price1))+(int(units2)*float(price2))
print('VALOR A PAGAR: R$ {:.2f}'.format(calculate_paid_amount))