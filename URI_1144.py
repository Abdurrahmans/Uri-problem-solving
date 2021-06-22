n = int(input())
x = 1
for i in range(n):
    for j in range(1):
        x1 = x**2
        x2 = x*x1
        print('{0} {1} {2}'.format(x, x1, x2))
        print('{0} {1} {2}'.format(x, x1+1, x2+1))
    x = x + 1