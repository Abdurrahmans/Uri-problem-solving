salary = float(input())
if salary>= 0 and salary<=400.00:
    bonus = salary*.15
    salary=salary+bonus
    print('Novo salario: {:.2f}'.format(salary))
    print('Reajuste ganho: {:.2f}'.format(bonus))
    print('Em percentual: 15 %')
elif salary>=400.01 and salary<=800.00:
    bonus = salary*.12
    salary=salary+bonus
    print('Novo salario: {:.2f}'.format(salary))
    print('Reajuste ganho: {:.2f}'.format(bonus))
    print('Em percentual: 12 %')
elif salary>=100.01 and salary<=1200.00:
    bonus = salary*.10
    salary=salary+bonus
    print('Novo salario: {:.2f}'.format(salary))
    print('Reajuste ganho: {:.2f}'.format(bonus))
    print('Em percentual: 10 %')
elif salary>=1200.01 and salary<=2000.00:
    bonus = salary*.07
    salary=salary+bonus
    print('Novo salario: {:.2f}'.format(salary))
    print('Reajuste ganho: {:.2f}'.format(bonus))
    print('Em percentual: 7 %')
elif salary>2000.00:
    bonus = salary*.04
    salary=salary+bonus
    print('Novo salario: {:.2f}'.format(salary))
    print('Reajuste ganho: {:.2f}'.format(bonus))
    print('Em percentual: 4 %')