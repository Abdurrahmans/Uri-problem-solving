salary = float(input())

if salary>=0 and salary<=2000.00:
    print('Isento')
elif salary>2000.00 and salary<=3000.00:
    salary -=2000.00
    result = (salary*0.08)
    print('R$ {:.2f}'.format(result))
elif salary>3000.00 and salary<=4500.00:
    salary -=3000.00
    result = (salary*.18)+(1000*0.08)
    print('R$ {:.2f}'.format(result))
else:
    salary -=4500.00
    result = (salary*0.28)+(1500*0.18)+(1000*0.08)
    print('R$ {:.2f}'.format(result))
